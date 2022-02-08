import os
import os.path as osp
import glob
import onnxruntime
from .arcface_onnx import *
from .retinaface import *
from .retinaface_trt import *
from .landmark import *
from .attribute import Attribute
from ..utils import download_onnx

__all__ = ['get_model']


class ModelRouter:
    def __init__(self, onnx_file):
        self.onnx_file = onnx_file

    def get_model(self, **kwargs):
        session = onnxruntime.InferenceSession(self.onnx_file, **kwargs)
        input_cfg = session.get_inputs()[0]
        input_shape = input_cfg.shape
        outputs = session.get_outputs()

        if len(outputs) >= 5:
            return RetinaFace(model_file=self.onnx_file, session=session)
        elif input_shape[2] == 112 and input_shape[3] == 112:
            return ArcFaceONNX(model_file=self.onnx_file, session=session)
        elif input_shape[2] == 192 and input_shape[3] == 192:
            return Landmark(model_file=self.onnx_file, session=session)
        elif input_shape[2] == 96 and input_shape[3] == 96:
            return Attribute(model_file=self.onnx_file, session=session)
        else:
            return None


def find_onnx_file(dir_path):
    if not os.path.exists(dir_path):
        return None
    paths = glob.glob("%s/*.onnx" % dir_path)
    if len(paths) == 0:
        return None
    paths = sorted(paths)
    return paths[-1]


def get_model(name, **kwargs):
    root = kwargs.get('root', '~/.insightface')
    root = os.path.expanduser(root)
    model_root = osp.join(root, 'models')
    allow_download = kwargs.get('download', False)
    if not name.endswith('.onnx'):
        model_dir = os.path.join(model_root, name)
        model_file = find_onnx_file(model_dir)
        if model_file is None:
            return None
    else:
        model_file = name
    if not osp.exists(model_file) and allow_download:
        model_file = download_onnx('models', model_file, root=root)
    assert osp.exists(model_file), 'model_file should exist'
    assert osp.isfile(model_file), 'model_file should be file'
    router = ModelRouter(model_file)
    model = router.get_model(providers=kwargs.get('providers'), provider_options=kwargs.get('provider_options'))
    return model
