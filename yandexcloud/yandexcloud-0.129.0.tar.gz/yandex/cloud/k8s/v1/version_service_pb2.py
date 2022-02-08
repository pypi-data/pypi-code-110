# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/k8s/v1/version_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.k8s.v1 import cluster_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_cluster__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/k8s/v1/version_service.proto',
  package='yandex.cloud.k8s.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8s',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)yandex/cloud/k8s/v1/version_service.proto\x12\x13yandex.cloud.k8s.v1\x1a\x1cgoogle/api/annotations.proto\x1a!yandex/cloud/k8s/v1/cluster.proto\"\x15\n\x13ListVersionsRequest\"Z\n\x14ListVersionsResponse\x12\x42\n\x12\x61vailable_versions\x18\x01 \x03(\x0b\x32&.yandex.cloud.k8s.v1.AvailableVersions\"c\n\x11\x41vailableVersions\x12<\n\x0frelease_channel\x18\x01 \x01(\x0e\x32#.yandex.cloud.k8s.v1.ReleaseChannel\x12\x10\n\x08versions\x18\x02 \x03(\t2\x97\x01\n\x0eVersionService\x12\x84\x01\n\x04List\x12(.yandex.cloud.k8s.v1.ListVersionsRequest\x1a).yandex.cloud.k8s.v1.ListVersionsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/managed-kubernetes/v1/versionsBV\n\x17yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8sb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_k8s_dot_v1_dot_cluster__pb2.DESCRIPTOR,])




_LISTVERSIONSREQUEST = _descriptor.Descriptor(
  name='ListVersionsRequest',
  full_name='yandex.cloud.k8s.v1.ListVersionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=152,
)


_LISTVERSIONSRESPONSE = _descriptor.Descriptor(
  name='ListVersionsResponse',
  full_name='yandex.cloud.k8s.v1.ListVersionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='available_versions', full_name='yandex.cloud.k8s.v1.ListVersionsResponse.available_versions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=244,
)


_AVAILABLEVERSIONS = _descriptor.Descriptor(
  name='AvailableVersions',
  full_name='yandex.cloud.k8s.v1.AvailableVersions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='release_channel', full_name='yandex.cloud.k8s.v1.AvailableVersions.release_channel', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='versions', full_name='yandex.cloud.k8s.v1.AvailableVersions.versions', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=345,
)

_LISTVERSIONSRESPONSE.fields_by_name['available_versions'].message_type = _AVAILABLEVERSIONS
_AVAILABLEVERSIONS.fields_by_name['release_channel'].enum_type = yandex_dot_cloud_dot_k8s_dot_v1_dot_cluster__pb2._RELEASECHANNEL
DESCRIPTOR.message_types_by_name['ListVersionsRequest'] = _LISTVERSIONSREQUEST
DESCRIPTOR.message_types_by_name['ListVersionsResponse'] = _LISTVERSIONSRESPONSE
DESCRIPTOR.message_types_by_name['AvailableVersions'] = _AVAILABLEVERSIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListVersionsRequest = _reflection.GeneratedProtocolMessageType('ListVersionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVERSIONSREQUEST,
  '__module__' : 'yandex.cloud.k8s.v1.version_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.ListVersionsRequest)
  })
_sym_db.RegisterMessage(ListVersionsRequest)

ListVersionsResponse = _reflection.GeneratedProtocolMessageType('ListVersionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVERSIONSRESPONSE,
  '__module__' : 'yandex.cloud.k8s.v1.version_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.ListVersionsResponse)
  })
_sym_db.RegisterMessage(ListVersionsResponse)

AvailableVersions = _reflection.GeneratedProtocolMessageType('AvailableVersions', (_message.Message,), {
  'DESCRIPTOR' : _AVAILABLEVERSIONS,
  '__module__' : 'yandex.cloud.k8s.v1.version_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.AvailableVersions)
  })
_sym_db.RegisterMessage(AvailableVersions)


DESCRIPTOR._options = None

_VERSIONSERVICE = _descriptor.ServiceDescriptor(
  name='VersionService',
  full_name='yandex.cloud.k8s.v1.VersionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=348,
  serialized_end=499,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.k8s.v1.VersionService.List',
    index=0,
    containing_service=None,
    input_type=_LISTVERSIONSREQUEST,
    output_type=_LISTVERSIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002!\022\037/managed-kubernetes/v1/versions',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VERSIONSERVICE)

DESCRIPTOR.services_by_name['VersionService'] = _VERSIONSERVICE

# @@protoc_insertion_point(module_scope)
