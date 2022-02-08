# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/httpbody.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/httpbody.proto',
  package='google.api',
  syntax='proto3',
  serialized_options=b'\n\016com.google.apiB\rHttpBodyProtoP\001Z;google.golang.org/genproto/googleapis/api/httpbody;httpbody\370\001\001\242\002\004GAPI',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19google/api/httpbody.proto\x12\ngoogle.api\x1a\x19google/protobuf/any.proto\"X\n\x08HttpBody\x12\x14\n\x0c\x63ontent_type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12(\n\nextensions\x18\x03 \x03(\x0b\x32\x14.google.protobuf.AnyBh\n\x0e\x63om.google.apiB\rHttpBodyProtoP\x01Z;google.golang.org/genproto/googleapis/api/httpbody;httpbody\xf8\x01\x01\xa2\x02\x04GAPIb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_HTTPBODY = _descriptor.Descriptor(
  name='HttpBody',
  full_name='google.api.HttpBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_type', full_name='google.api.HttpBody.content_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='google.api.HttpBody.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extensions', full_name='google.api.HttpBody.extensions', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=68,
  serialized_end=156,
)

_HTTPBODY.fields_by_name['extensions'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['HttpBody'] = _HTTPBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HttpBody = _reflection.GeneratedProtocolMessageType('HttpBody', (_message.Message,), {
  'DESCRIPTOR' : _HTTPBODY,
  '__module__' : 'google.api.httpbody_pb2'
  # @@protoc_insertion_point(class_scope:google.api.HttpBody)
  })
_sym_db.RegisterMessage(HttpBody)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
