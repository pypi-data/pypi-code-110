# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/evidence/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/evidence/v1beta1/genesis.proto',
  package='cosmos.evidence.v1beta1',
  syntax='proto3',
  serialized_options=b'Z-github.com/cosmos/cosmos-sdk/x/evidence/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%cosmos/evidence/v1beta1/genesis.proto\x12\x17\x63osmos.evidence.v1beta1\x1a\x19google/protobuf/any.proto\"6\n\x0cGenesisState\x12&\n\x08\x65vidence\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB/Z-github.com/cosmos/cosmos-sdk/x/evidence/typesb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.evidence.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='evidence', full_name='cosmos.evidence.v1beta1.GenesisState.evidence', index=0,
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
  serialized_start=93,
  serialized_end=147,
)

_GENESISSTATE.fields_by_name['evidence'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.evidence.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.evidence.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
