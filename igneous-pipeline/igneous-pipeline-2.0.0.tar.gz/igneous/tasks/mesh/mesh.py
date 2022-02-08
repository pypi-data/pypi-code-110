from collections import defaultdict
import json
import math
import os
import random
import re
from typing import Optional, Tuple, Union

import numpy as np
import scipy.ndimage
from tqdm import tqdm

from cloudfiles import CloudFiles
import cloudfiles.paths

from cloudvolume import CloudVolume, view
from cloudvolume.lib import Vec, Bbox, jsonify
import mapbuffer
from mapbuffer import MapBuffer
from taskqueue import RegisteredTask, queueable

import cc3d
import DracoPy
import fastremap
import zmesh

from .draco import calculate_draco_quantization_bits_and_range, draco_encoding_settings
from . import mesh_graphene_remap

__all__ = [
  "MeshTask", "GrapheneMeshTask", 
  "MeshManifestPrefixTask", "MeshManifestFilesystemTask",
  "MeshSpatialIndex", "TransferMeshFilesTask",
]

def find_objects(labels):
  """  
  scipy.ndimage.find_objects performs about 7-8x faster on C 
  ordered arrays, so we just do it that way and convert
  the results if it's in F order.
  """
  if labels.flags.c_contiguous:
    return scipy.ndimage.find_objects(labels)
  else:
    all_slices = scipy.ndimage.find_objects(labels.T)
    return [ (slcs and slcs[::-1]) for slcs in all_slices ]

class MeshTask(RegisteredTask):
  def __init__(self, shape, offset, layer_path, **kwargs):
    """
    Convert all labels in the specified bounding box into meshes
    via marching cubes and quadratic edge collapse (github.com/seung-lab/zmesh).

    Required:
      shape: (sx,sy,sz) size of task
      offset: (x,y,z) offset from (0,0,0)
      layer_path: neuroglancer/cloudvolume dataset path

    Optional:
      lod: (uint) level of detail to record these meshes at
      mip: (uint) level of the resolution pyramid to download segmentation from
      simplification_factor: (uint) try to reduce the number of triangles in the 
        mesh by this factor (but constrained by max_simplification_error)
      max_simplification_error: The maximum physical distance that
        simplification is allowed to move a triangle vertex by. 
      mesh_dir: which subdirectory to write the meshes to (overrides info file location)
      remap_table: agglomerate segmentation before meshing using { orig_id: new_id }
      generate_manifests: (bool) if it is known that the meshes generated by this 
        task will not be cropped by the bounding box, avoid needing to run a seperate
        MeshManifestTask pass by generating manifests on the spot.

      These two options are used to allow sufficient overlap for trivial mesh stitching
      between adjacent tasks.

        low_padding: (uint) expand the bounding box by this many pixels by subtracting
          this padding from the minimum point of the bounding box on all axes.
        high_padding: (uint) expand the bounding box by this many pixels adding
          this padding to the maximum point of the bounding box on all axes.

      parallel_download: (uint: 1) number of processes to use during the segmentation download
      cache_control: (str: None) specify the cache-control header when uploading mesh files
      dust_threshold: (uint: None) don't bother meshing labels strictly smaller than this number of voxels.
      encoding: (str) 'precomputed' (default) or 'draco'
      draco_compression_level: (uint: 1) only applies to draco encoding
      draco_create_metadata: (bool: False) only applies to draco encoding
      progress: (bool: False) show progress bars for meshing 
      object_ids: (list of ints) if specified, only mesh these ids
      fill_missing: (bool: False) replace missing segmentation files with zeros instead of erroring
      spatial_index: (bool: False) generate a JSON spatial index of which meshes are available in
        a given bounding box. 
      sharded: (bool: False) If True, upload all meshes together as a single mapbuffer 
        fragment file. 
      timestamp: (int: None) (graphene only) use the segmentation existing at this
        UNIX timestamp.
    """
    super(MeshTask, self).__init__(shape, offset, layer_path, **kwargs)
    self.shape = Vec(*shape)
    self.offset = Vec(*offset)
    self.layer_path = layer_path
    self.options = {
      'cache_control': kwargs.get('cache_control', None),
      'draco_compression_level': kwargs.get('draco_compression_level', 1),
      'draco_create_metadata': kwargs.get('draco_create_metadata', False),
      'dust_threshold': kwargs.get('dust_threshold', None),
      'encoding': kwargs.get('encoding', 'precomputed'),
      'fill_missing': kwargs.get('fill_missing', False),
      'generate_manifests': kwargs.get('generate_manifests', False),
      'high_padding': kwargs.get('high_padding', 1),
      'low_padding': kwargs.get('low_padding', 0),
      'lod': kwargs.get('lod', 0),
      'max_simplification_error': kwargs.get('max_simplification_error', 40),
      'simplification_factor': kwargs.get('simplification_factor', 100),
      'mesh_dir': kwargs.get('mesh_dir', None),
      'mip': kwargs.get('mip', 0),
      'object_ids': kwargs.get('object_ids', None),
      'parallel_download': kwargs.get('parallel_download', 1),
      'progress': kwargs.get('progress', False),
      'remap_table': kwargs.get('remap_table', None),
      'spatial_index': kwargs.get('spatial_index', False),
      'sharded': kwargs.get('sharded', False),
      'timestamp': kwargs.get('timestamp', None),
      'agglomerate': kwargs.get('agglomerate', True),
      'stop_layer': kwargs.get('stop_layer', 2),
      'compress': kwargs.get('compress', 'gzip'),
      'closed_dataset_edges': kwargs.get('closed_dataset_edges', True),
    }
    supported_encodings = ['precomputed', 'draco']
    if not self.options['encoding'] in supported_encodings:
      raise ValueError('Encoding {} is not supported. Options: {}'.format(
        self.options['encoding'], ', '.join(supported_encodings)
      ))
    self._encoding_to_compression_dict = {
      'precomputed': self.options['compress'],
      'draco': False,
    }

  def execute(self):
    self._volume = CloudVolume(
      self.layer_path, self.options['mip'], bounded=False,
      parallel=self.options['parallel_download'], 
      fill_missing=self.options['fill_missing']
    )
    self._bounds = Bbox(self.offset, self.shape + self.offset)
    self._bounds = Bbox.clamp(self._bounds, self._volume.bounds)

    self.progress = bool(self.options['progress'])

    self._mesher = zmesh.Mesher(self._volume.resolution)

    # Marching cubes loves its 1vx overlaps.
    # This avoids lines appearing between
    # adjacent chunks.
    data_bounds = self._bounds.clone()
    data_bounds.minpt -= self.options['low_padding']
    data_bounds.maxpt += self.options['high_padding']

    self._mesh_dir = self.get_mesh_dir()

    if self.options['encoding'] == 'draco':
      self.draco_encoding_settings = draco_encoding_settings(
        shape=(self.shape + self.options['low_padding'] + self.options['high_padding']),
        offset=self.offset,
        resolution=self._volume.resolution,
        compression_level=self.options["draco_compression_level"],
        create_metadata=self.options['draco_create_metadata'],
        uses_new_draco_bin_size=False,
      )

    # chunk_position includes the overlap specified by low_padding/high_padding
    # agglomerate, timestamp, stop_layer only applies to graphene volumes, 
    # no-op for precomputed
    data = self._volume.download(
      data_bounds, 
      agglomerate=self.options['agglomerate'], 
      timestamp=self.options['timestamp'], 
      stop_layer=self.options['stop_layer']
    )

    if not np.any(data):
      if self.options['spatial_index']:
        self._upload_spatial_index(self._bounds, {})
      return

    left_offset = Vec(0,0,0)
    if self.options["closed_dataset_edges"]:
      data, left_offset = self._handle_dataset_boundary(data, data_bounds)

    data = self._remove_dust(data, self.options['dust_threshold'])
    data = self._remap(data)

    if self.options['object_ids']:
      data = fastremap.mask_except(data, self.options['object_ids'], in_place=True)

    data, renumbermap = fastremap.renumber(data, in_place=True)
    renumbermap = { v:k for k,v in renumbermap.items() }

    data = fastremap.ascontiguousarray(data[..., 0].T)
    self._mesher.mesh(data)
    del data

    self.compute_meshes(renumbermap, left_offset)

  def _handle_dataset_boundary(self, data, bbox):
    """
    This logic is used to add a black border along sides
    of the image that touch the dataset boundary which
    results in the closure of the mesh faces on that side.
    """
    if (
      (not np.any(bbox.minpt == self._volume.bounds.minpt))
      and (not np.any(bbox.maxpt == self._volume.bounds.maxpt))
    ):
      return data, Vec(0,0,0)

    shape = Vec(*data.shape, dtype=np.int64)
    offset = Vec(0,0,0,0)
    for i in range(3):
      if bbox.minpt[i] == self._volume.voxel_offset[i]:
        offset[i] += 1
        shape[i] += 1
      if bbox.maxpt[i] == self._volume.bounds.maxpt[i]:
        shape[i] += 1

    slices = (
      slice(offset.x, offset.x + data.shape[0]),
      slice(offset.y, offset.y + data.shape[1]),
      slice(offset.z, offset.z + data.shape[2]),
    )

    mirror_data = np.zeros(shape, dtype=data.dtype, order="F")
    mirror_data[slices] = data
    if offset[0]:
      mirror_data[0,:,:] = 0
    if offset[1]:
      mirror_data[:,0,:] = 0
    if offset[2]:
      mirror_data[:,:,0] = 0

    return mirror_data, offset[:3]

  def get_mesh_dir(self):
    if self.options['mesh_dir'] is not None:
      return self.options['mesh_dir']
    elif 'mesh' in self._volume.info:
      return self._volume.info['mesh']
    else:
      raise ValueError("The mesh destination is not present in the info file.")

  def _remove_dust(self, data, dust_threshold):
    if dust_threshold:
      segids, pxct = fastremap.unique(data, return_counts=True)
      dust_segids = [ sid for sid, ct in zip(segids, pxct) if ct < int(dust_threshold) ]
      data = fastremap.mask(data, dust_segids, in_place=True)

    return data

  def _remap(self, data):
    if self.options['remap_table'] is None:
      return data 

    self.options['remap_table'] = {
      int(k): int(v) for k, v in self.options['remap_table'].items()
    }

    remap = self.options['remap_table']
    remap[0] = 0

    data = fastremap.mask_except(data, list(remap.keys()), in_place=True)
    return fastremap.remap(data, remap, in_place=True)

  def compute_meshes(self, renumbermap, offset):
    bounding_boxes = {}
    meshes = {}

    for obj_id in tqdm(self._mesher.ids(), disable=(not self.progress), desc="Mesh"):
      remapped_id = renumbermap[obj_id]
      mesh_binary, mesh_bounds = self._create_mesh(obj_id, offset)
      bounding_boxes[remapped_id] = mesh_bounds.to_list()
      meshes[remapped_id] = mesh_binary

    if self.options['sharded']:
      self._upload_batch(meshes, self._bounds)
    else:
      self._upload_individuals(meshes, self.options['generate_manifests'])

    if self.options['spatial_index']:
      self._upload_spatial_index(self._bounds, bounding_boxes)

  def _upload_batch(self, meshes, bbox):
    cf = CloudFiles(self.layer_path, progress=self.options['progress'])

    mbuf = MapBuffer(meshes, compress="br")

    cf.put(
      f"{self._mesh_dir}/{bbox.to_filename()}.frags",
      content=mbuf.tobytes(),
      compress=None,
      content_type="application/x.mapbuffer",
      cache_control=False,
    )

  def _upload_individuals(self, mesh_binaries, generate_manifests):
    cf = CloudFiles(self.layer_path)

    content_type = "model/mesh"
    if self.options["encoding"] == "draco":
      content_type = "model/x.draco"
    
    cf.puts(
      ( 
        (
          f"{self._mesh_dir}/{segid}:{self.options['lod']}:{self._bounds.to_filename()}", 
          mesh_binary
        ) 
        for segid, mesh_binary in mesh_binaries.items() 
      ),
      compress=self._encoding_to_compression_dict[self.options['encoding']],
      cache_control=self.options['cache_control'],
      content_type=content_type,
    )

    if generate_manifests:
      cf.put_jsons(
        (
          (
            f"{self._mesh_dir}/{segid}:{self.options['lod']}", 
            { "fragments": [ f"{segid}:{self.options['lod']}:{self._bounds.to_filename()}" ] }
          )
          for segid, mesh_binary in mesh_binaries.items()
        ),
        compress=None,
        cache_control=self.options['cache_control'],
      )

  def _create_mesh(self, obj_id, left_bound_offset):
    mesh = self._mesher.get_mesh(
      obj_id,
      simplification_factor=self.options['simplification_factor'],
      max_simplification_error=self.options['max_simplification_error'],
      voxel_centered=True,
    )

    self._mesher.erase(obj_id)

    resolution = self._volume.resolution
    offset = (self._bounds.minpt - self.options['low_padding']).astype(np.float32)
    mesh.vertices[:] += (offset - left_bound_offset) * resolution

    mesh_bounds = Bbox(
      np.amin(mesh.vertices, axis=0), 
      np.amax(mesh.vertices, axis=0)
    )

    if self.options['encoding'] == 'draco':
      mesh_binary = DracoPy.encode(
        mesh.vertices, mesh.faces, 
        **self.draco_encoding_settings
      )
    elif self.options['encoding'] == 'precomputed':
      mesh_binary = mesh.to_precomputed()

    return mesh_binary, mesh_bounds

  def _upload_spatial_index(self, bbox, mesh_bboxes):
    cf = CloudFiles(self.layer_path, progress=self.options['progress'])
    precision = self._volume.mesh.spatial_index.precision
    resolution = self._volume.resolution 

    bbox = bbox.astype(resolution.dtype) * resolution

    cf.put_json(
      f"{self._mesh_dir}/{bbox.to_filename(precision)}.spatial",
      mesh_bboxes,
      compress=self.options['compress'],
      cache_control=False,
    )

class GrapheneMeshTask(RegisteredTask):
  def __init__(self, cloudpath, shape, offset, mip, **kwargs):
    """
    Convert all labels in the specified bounding box into meshes
    via marching cubes and quadratic edge collapse (github.com/seung-lab/zmesh).

    Required:
      shape: (sx,sy,sz) size of task
      offset: (x,y,z) offset from (0,0,0)
      cloudpath: neuroglancer/cloudvolume dataset path

    Optional:
      mip: (uint) level of the resolution pyramid to download segmentation from
      simplification_factor: (uint) try to reduce the number of triangles in the 
        mesh by this factor (but constrained by max_simplification_error)
      max_simplification_error: The maximum physical distance that
        simplification is allowed to move a triangle vertex by. 
      mesh_dir: which subdirectory to write the meshes to (overrides info file location)

      parallel_download: (uint: 1) number of processes to use during the segmentation download
      cache_control: (str: None) specify the cache-control header when uploading mesh files
      dust_threshold: (uint: None) don't bother meshing labels strictly smaller than this number of voxels.
      encoding: (str) 'precomputed' (default) or 'draco'
      draco_compression_level: (uint: 1) only applies to draco encoding
      progress: (bool: False) show progress bars for meshing 
      object_ids: (list of ints) if specified, only mesh these ids
      fill_missing: (bool: False) replace missing segmentation files with zeros instead of erroring
      timestamp: (int: None) (graphene only) use the segmentation existing at this
        UNIX timestamp.
    """
    super(GrapheneMeshTask, self).__init__(cloudpath, shape, offset, mip, **kwargs)
    self.shape = Vec(*shape)
    self.offset = Vec(*offset)
    self.mip = int(mip)
    self.cloudpath = cloudpath
    self.layer_id = 2
    self.overlap_vx = 1
    self.options = {
      'cache_control': kwargs.get('cache_control', None),
      'draco_compression_level': kwargs.get('draco_compression_level', 1),
      'fill_missing': kwargs.get('fill_missing', False),
      'max_simplification_error': kwargs.get('max_simplification_error', 40),
      'simplification_factor': kwargs.get('simplification_factor', 100),
      'mesh_dir': kwargs.get('mesh_dir', None),
      'progress': kwargs.get('progress', False),
      'timestamp': kwargs.get('timestamp', None),
    }

  def execute(self):
    self.cv = CloudVolume(
      self.cloudpath, mip=self.mip, bounded=False,
      fill_missing=self.options['fill_missing'],
      mesh_dir=self.options['mesh_dir'],
    )

    if self.cv.mesh.meta.is_sharded() == False:
      raise ValueError("The mesh sharding parameter must be defined.")

    self.bounds = Bbox(self.offset, self.shape + self.offset)
    self.bounds = Bbox.clamp(self.bounds, self.cv.bounds)

    self.progress = bool(self.options['progress'])

    self.mesher = zmesh.Mesher(self.cv.resolution)

    # Marching cubes needs 1 voxel overlap to properly 
    # stitch adjacent meshes.
    # data_bounds = self.bounds.clone()
    # data_bounds.maxpt += self.overlap_vx

    self.mesh_dir = self.get_mesh_dir()
    self.draco_encoding_settings = draco_encoding_settings(
      shape=(self.shape + self.overlap_vx),
      offset=self.offset,
      resolution=self.cv.resolution,
      compression_level=1,
      create_metadata=True,
      uses_new_draco_bin_size=self.cv.meta.uses_new_draco_bin_size,
    )

    chunk_pos = self.cv.meta.point_to_chunk_position(self.bounds.center(), mip=self.mip)
    
    img = mesh_graphene_remap.remap_segmentation(
      self.cv, 
      chunk_pos.x, chunk_pos.y, chunk_pos.z, 
      mip=self.mip, 
      overlap_vx=self.overlap_vx, 
      time_stamp=self.timestamp,
      progress=self.progress,
    )

    if not np.any(img):
      return

    self.upload_meshes(
      self.compute_meshes(img)
    )

  def get_mesh_dir(self):
    if self.options['mesh_dir'] is not None:
      return self.options['mesh_dir']
    elif 'mesh' in self.cv.info:
      return self.cv.info['mesh']
    else:
      raise ValueError("The mesh destination is not present in the info file.")

  def compute_meshes(self, data):
    data = data.T
    self.mesher.mesh(data)
    del data

    meshes = {}
    for obj_id in tqdm(self.mesher.ids(), disable=(not self.progress), desc="Mesh"):
      # remapped_id = component_map[obj_id]
      meshes[obj_id] = self.create_mesh(obj_id)

    return meshes

  def upload_meshes(self, meshes):
    if len(meshes) == 0:
      return

    reader = self.cv.mesh.readers[self.layer_id] 

    shard_binary = reader.spec.synthesize_shard(meshes)
    # the shard filename is derived from the chunk position,
    # so any label inside this L2 chunk will do
    shard_filename = reader.get_filename(list(meshes.keys())[0]) 

    cf = CloudFiles(self.cv.cloudpath)
    cf.put(
      f"{self.get_mesh_dir()}/initial/{self.layer_id}/{shard_filename}",
      shard_binary,
      compress=None,
      content_type="application/octet-stream",
      cache_control="no-cache",
    )

  def create_mesh(self, obj_id):
    mesh = self.mesher.get_mesh(
      obj_id,
      simplification_factor=self.options['simplification_factor'],
      max_simplification_error=self.options['max_simplification_error'],
      # Graphene meshes were created before we fixed the offset problem
      # so unless otherwise specificed, keep this set to False
      voxel_centered=False, 
    )

    self.mesher.erase(obj_id)
    mesh.vertices[:] += self.bounds.minpt * self.cv.resolution

    mesh_binary = DracoPy.encode(
      mesh.vertices, mesh.faces, 
      **self.draco_encoding_settings
    )

    return mesh_binary

@queueable
def MeshManifestFilesystemTask(
  layer_path:str,
  lod:int = 0,
  mesh_dir:Optional[str] = None,
):
  cf = CloudFiles(layer_path)
  info = cf.get_json('info')

  if mesh_dir is None and 'mesh' in info:
    mesh_dir = info['mesh']

  filepath = cloudfiles.paths.asfilepath(
    cf.join(layer_path, mesh_dir)
  )
  segids = defaultdict(list)

  regexp = re.compile(r'(\d+):(\d+):')
  for entry in os.scandir(filepath):
    if not entry.is_file():
      continue

    filename = os.path.basename(entry.name)
    # `match` implies the beginning (^). `search` matches whole string
    matches = re.search(regexp, filename)

    if not matches:
      continue

    segid, mlod = matches.groups()
    segid, mlod = int(segid), int(mlod)

    if mlod != lod:
      continue

    filename, ext = os.path.splitext(filename)
    segids[segid].append(filename)

  items = ( 
    (
      f"{mesh_dir}/{segid}:{lod}", 
      { "fragments": frags }
    ) 
    for segid, frags in segids.items() 
  )

  cf.put_jsons(items)

@queueable
def MeshManifestPrefixTask(
  layer_path:str, 
  prefix:str,
  lod:int = 0, 
  mesh_dir:Optional[str] = None
):
  """
  Finalize mesh generation by post-processing chunk fragment
  lists into mesh fragment manifests.
  These are necessary for neuroglancer to know which mesh
  fragments to download for a given segid.

  If we parallelize using prefixes single digit prefixes ['0','1',..'9'] all meshes will
  be correctly processed. But if we do ['10','11',..'99'] meshes from [0,9] won't get
  processed and need to be handle specifically by creating tasks that will process
  a single mesh ['0:','1:',..'9:']
  """
  cf = CloudFiles(layer_path)
  info = cf.get_json('info')

  if mesh_dir is None and 'mesh' in info:
    mesh_dir = info['mesh']

  prefix = cf.join(mesh_dir, prefix)
  segids = defaultdict(list)

  regexp = re.compile(r'(\d+):(\d+):')
  for filename in cf.list(prefix=prefix):
    filename = os.path.basename(filename)
    # `match` implies the beginning (^). `search` matches whole string
    matches = re.search(regexp, filename)

    if not matches:
      continue

    segid, mlod = matches.groups()
    segid, mlod = int(segid), int(mlod)

    if mlod != lod:
      continue

    segids[segid].append(filename)

  items = ( 
    (
      f"{mesh_dir}/{segid}:{lod}", 
      { "fragments": frags }
    ) 
    for segid, frags in segids.items() 
  )

  cf.put_jsons(items)

@queueable
def MeshSpatialIndex(
  cloudpath:str, 
  shape:Tuple[int,int,int], 
  offset:Tuple[int,int,int], 
  mip:int = 0, 
  fill_missing:bool=False, 
  compress:Optional[Union[str,bool]] = 'gzip', 
  mesh_dir:Optional[str] = None
) -> None:
  """
  The main way to add a spatial index is to use the MeshTask,
  but old datasets or broken datasets may need it to be 
  reconstituted. An alternative use is create the spatial index
  over a different area size than the mesh task.
  """
  cv = CloudVolume(
    cloudpath, mip=mip, 
    bounded=False, fill_missing=fill_missing
  )
  cf = CloudFiles(cloudpath)

  bounds = Bbox(Vec(*offset), Vec(*shape) + Vec(*offset))
  bounds = Bbox.clamp(bounds, cv.bounds)

  data_bounds = bounds.clone()
  data_bounds.maxpt += 1 # match typical Marching Cubes overlap

  precision = cv.mesh.spatial_index.precision
  resolution = cv.resolution 

  if not mesh_dir:
    mesh_dir = cv.info["mesh"]

  # remap: old img -> img
  img, remap = cv.download(data_bounds, renumber=True)
  img = img[...,0]
  slcs = find_objects(img)
  del img
  reverse_map = { v:k for k,v in remap.items() } # img -> old img

  bboxes = {}
  for label, slc in enumerate(slcs):
    if slc is None:
      continue
    mesh_bounds = Bbox.from_slices(slc)
    mesh_bounds += Vec(*offset)
    mesh_bounds *= Vec(*resolution, dtype=np.float32)
    bboxes[str(reverse_map[label+1])] = \
      mesh_bounds.astype(resolution.dtype).to_list()

  bounds = bounds.astype(resolution.dtype) * resolution
  cf.put_json(
    f"{mesh_dir}/{bounds.to_filename(precision)}.spatial",
    bboxes,
    compress=compress,
    cache_control=False,
  )

@queueable
def TransferMeshFilesTask(
  src:str,
  dest:str,
  prefix:str,
  mesh_dir:Optional[str] = None
):
  cv_src = CloudVolume(src)
  cv_dest = CloudVolume(dest, mesh_dir=mesh_dir)

  cf_src = CloudFiles(cv_src.mesh.meta.layerpath)
  cf_dest = CloudFiles(cv_dest.mesh.meta.layerpath)

  cf_src.transfer_to(cf_dest, paths=cf_src.list(prefix=prefix))















