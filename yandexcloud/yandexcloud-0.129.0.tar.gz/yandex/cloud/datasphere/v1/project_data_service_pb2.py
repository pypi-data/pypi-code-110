# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v1/project_data_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datasphere/v1/project_data_service.proto',
  package='yandex.cloud.datasphere.v1',
  syntax='proto3',
  serialized_options=b'\n\036yandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphere',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5yandex/cloud/datasphere/v1/project_data_service.proto\x12\x1ayandex.cloud.datasphere.v1\x1a\x1dyandex/cloud/validation.proto\"S\n\x0c\x46ileMetadata\x12!\n\nproject_id\x18\x01 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05<=200\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x12\n\nsize_bytes\x18\x03 \x01(\x03\"m\n\x11UploadFileRequest\x12<\n\x08metadata\x18\x01 \x01(\x0b\x32(.yandex.cloud.datasphere.v1.FileMetadataH\x00\x12\x0f\n\x05\x63hunk\x18\x02 \x01(\x0cH\x00\x42\t\n\x07message\"P\n\x12UploadFileResponse\x12:\n\x08metadata\x18\x01 \x01(\x0b\x32(.yandex.cloud.datasphere.v1.FileMetadata\"Q\n\x13\x44ownloadFileRequest\x12!\n\nproject_id\x18\x01 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05<=200\x12\x17\n\tfile_path\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"p\n\x14\x44ownloadFileResponse\x12<\n\x08metadata\x18\x01 \x01(\x0b\x32(.yandex.cloud.datasphere.v1.FileMetadataH\x00\x12\x0f\n\x05\x63hunk\x18\x02 \x01(\x0cH\x00\x42\t\n\x07message2\xf8\x01\n\x12ProjectDataService\x12m\n\nUploadFile\x12-.yandex.cloud.datasphere.v1.UploadFileRequest\x1a..yandex.cloud.datasphere.v1.UploadFileResponse(\x01\x12s\n\x0c\x44ownloadFile\x12/.yandex.cloud.datasphere.v1.DownloadFileRequest\x1a\x30.yandex.cloud.datasphere.v1.DownloadFileResponse0\x01\x42k\n\x1eyandex.cloud.api.datasphere.v1ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v1;datasphereb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_FILEMETADATA = _descriptor.Descriptor(
  name='FileMetadata',
  full_name='yandex.cloud.datasphere.v1.FileMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='yandex.cloud.datasphere.v1.FileMetadata.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\005<=200', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='yandex.cloud.datasphere.v1.FileMetadata.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size_bytes', full_name='yandex.cloud.datasphere.v1.FileMetadata.size_bytes', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=116,
  serialized_end=199,
)


_UPLOADFILEREQUEST = _descriptor.Descriptor(
  name='UploadFileRequest',
  full_name='yandex.cloud.datasphere.v1.UploadFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='yandex.cloud.datasphere.v1.UploadFileRequest.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='yandex.cloud.datasphere.v1.UploadFileRequest.chunk', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
    _descriptor.OneofDescriptor(
      name='message', full_name='yandex.cloud.datasphere.v1.UploadFileRequest.message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=201,
  serialized_end=310,
)


_UPLOADFILERESPONSE = _descriptor.Descriptor(
  name='UploadFileResponse',
  full_name='yandex.cloud.datasphere.v1.UploadFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='yandex.cloud.datasphere.v1.UploadFileResponse.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=312,
  serialized_end=392,
)


_DOWNLOADFILEREQUEST = _descriptor.Descriptor(
  name='DownloadFileRequest',
  full_name='yandex.cloud.datasphere.v1.DownloadFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='yandex.cloud.datasphere.v1.DownloadFileRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\005<=200', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='yandex.cloud.datasphere.v1.DownloadFileRequest.file_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=394,
  serialized_end=475,
)


_DOWNLOADFILERESPONSE = _descriptor.Descriptor(
  name='DownloadFileResponse',
  full_name='yandex.cloud.datasphere.v1.DownloadFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='yandex.cloud.datasphere.v1.DownloadFileResponse.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='yandex.cloud.datasphere.v1.DownloadFileResponse.chunk', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
    _descriptor.OneofDescriptor(
      name='message', full_name='yandex.cloud.datasphere.v1.DownloadFileResponse.message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=477,
  serialized_end=589,
)

_UPLOADFILEREQUEST.fields_by_name['metadata'].message_type = _FILEMETADATA
_UPLOADFILEREQUEST.oneofs_by_name['message'].fields.append(
  _UPLOADFILEREQUEST.fields_by_name['metadata'])
_UPLOADFILEREQUEST.fields_by_name['metadata'].containing_oneof = _UPLOADFILEREQUEST.oneofs_by_name['message']
_UPLOADFILEREQUEST.oneofs_by_name['message'].fields.append(
  _UPLOADFILEREQUEST.fields_by_name['chunk'])
_UPLOADFILEREQUEST.fields_by_name['chunk'].containing_oneof = _UPLOADFILEREQUEST.oneofs_by_name['message']
_UPLOADFILERESPONSE.fields_by_name['metadata'].message_type = _FILEMETADATA
_DOWNLOADFILERESPONSE.fields_by_name['metadata'].message_type = _FILEMETADATA
_DOWNLOADFILERESPONSE.oneofs_by_name['message'].fields.append(
  _DOWNLOADFILERESPONSE.fields_by_name['metadata'])
_DOWNLOADFILERESPONSE.fields_by_name['metadata'].containing_oneof = _DOWNLOADFILERESPONSE.oneofs_by_name['message']
_DOWNLOADFILERESPONSE.oneofs_by_name['message'].fields.append(
  _DOWNLOADFILERESPONSE.fields_by_name['chunk'])
_DOWNLOADFILERESPONSE.fields_by_name['chunk'].containing_oneof = _DOWNLOADFILERESPONSE.oneofs_by_name['message']
DESCRIPTOR.message_types_by_name['FileMetadata'] = _FILEMETADATA
DESCRIPTOR.message_types_by_name['UploadFileRequest'] = _UPLOADFILEREQUEST
DESCRIPTOR.message_types_by_name['UploadFileResponse'] = _UPLOADFILERESPONSE
DESCRIPTOR.message_types_by_name['DownloadFileRequest'] = _DOWNLOADFILEREQUEST
DESCRIPTOR.message_types_by_name['DownloadFileResponse'] = _DOWNLOADFILERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileMetadata = _reflection.GeneratedProtocolMessageType('FileMetadata', (_message.Message,), {
  'DESCRIPTOR' : _FILEMETADATA,
  '__module__' : 'yandex.cloud.datasphere.v1.project_data_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.FileMetadata)
  })
_sym_db.RegisterMessage(FileMetadata)

UploadFileRequest = _reflection.GeneratedProtocolMessageType('UploadFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADFILEREQUEST,
  '__module__' : 'yandex.cloud.datasphere.v1.project_data_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.UploadFileRequest)
  })
_sym_db.RegisterMessage(UploadFileRequest)

UploadFileResponse = _reflection.GeneratedProtocolMessageType('UploadFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADFILERESPONSE,
  '__module__' : 'yandex.cloud.datasphere.v1.project_data_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.UploadFileResponse)
  })
_sym_db.RegisterMessage(UploadFileResponse)

DownloadFileRequest = _reflection.GeneratedProtocolMessageType('DownloadFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADFILEREQUEST,
  '__module__' : 'yandex.cloud.datasphere.v1.project_data_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.DownloadFileRequest)
  })
_sym_db.RegisterMessage(DownloadFileRequest)

DownloadFileResponse = _reflection.GeneratedProtocolMessageType('DownloadFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADFILERESPONSE,
  '__module__' : 'yandex.cloud.datasphere.v1.project_data_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datasphere.v1.DownloadFileResponse)
  })
_sym_db.RegisterMessage(DownloadFileResponse)


DESCRIPTOR._options = None
_FILEMETADATA.fields_by_name['project_id']._options = None
_DOWNLOADFILEREQUEST.fields_by_name['project_id']._options = None
_DOWNLOADFILEREQUEST.fields_by_name['file_path']._options = None

_PROJECTDATASERVICE = _descriptor.ServiceDescriptor(
  name='ProjectDataService',
  full_name='yandex.cloud.datasphere.v1.ProjectDataService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=592,
  serialized_end=840,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadFile',
    full_name='yandex.cloud.datasphere.v1.ProjectDataService.UploadFile',
    index=0,
    containing_service=None,
    input_type=_UPLOADFILEREQUEST,
    output_type=_UPLOADFILERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadFile',
    full_name='yandex.cloud.datasphere.v1.ProjectDataService.DownloadFile',
    index=1,
    containing_service=None,
    input_type=_DOWNLOADFILEREQUEST,
    output_type=_DOWNLOADFILERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROJECTDATASERVICE)

DESCRIPTOR.services_by_name['ProjectDataService'] = _PROJECTDATASERVICE

# @@protoc_insertion_point(module_scope)
