# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: memory_profiling.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='memory_profiling.proto',
  package='mindspore.profiler',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16memory_profiling.proto\x12\x12mindspore.profiler\"V\n\x0bMemoryProto\x12\x34\n\tgraph_mem\x18\x01 \x03(\x0b\x32!.mindspore.profiler.GraphMemProto\x12\x11\n\ttotal_mem\x18\x02 \x01(\x04\"\xc5\x01\n\rGraphMemProto\x12\x10\n\x08graph_id\x18\x01 \x01(\x03\x12\x12\n\nstatic_mem\x18\x02 \x01(\x03\x12\x33\n\tnode_mems\x18\x03 \x03(\x0b\x32 .mindspore.profiler.NodeMemProto\x12\x37\n\x0btensor_mems\x18\x04 \x03(\x0b\x32\".mindspore.profiler.TensorMemProto\x12\x10\n\x08\x66p_start\x18\x05 \x01(\t\x12\x0e\n\x06\x62p_end\x18\x06 \x01(\t\"\x82\x01\n\x0cNodeMemProto\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x0f\n\x07node_id\x18\x02 \x01(\x04\x12\x17\n\x0finput_tensor_id\x18\x03 \x03(\x04\x12\x18\n\x10output_tensor_id\x18\x04 \x03(\x04\x12\x1b\n\x13workspace_tensor_id\x18\x05 \x03(\x04\"x\n\x0eTensorMemProto\x12\x11\n\ttensor_id\x18\x01 \x01(\x04\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x12\n\nlife_start\x18\x04 \x01(\x04\x12\x10\n\x08life_end\x18\x05 \x01(\x04\x12\x11\n\tlife_long\x18\x06 \x01(\tb\x06proto3'
)




_MEMORYPROTO = _descriptor.Descriptor(
  name='MemoryProto',
  full_name='mindspore.profiler.MemoryProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph_mem', full_name='mindspore.profiler.MemoryProto.graph_mem', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_mem', full_name='mindspore.profiler.MemoryProto.total_mem', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=46,
  serialized_end=132,
)


_GRAPHMEMPROTO = _descriptor.Descriptor(
  name='GraphMemProto',
  full_name='mindspore.profiler.GraphMemProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph_id', full_name='mindspore.profiler.GraphMemProto.graph_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='static_mem', full_name='mindspore.profiler.GraphMemProto.static_mem', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_mems', full_name='mindspore.profiler.GraphMemProto.node_mems', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tensor_mems', full_name='mindspore.profiler.GraphMemProto.tensor_mems', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fp_start', full_name='mindspore.profiler.GraphMemProto.fp_start', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bp_end', full_name='mindspore.profiler.GraphMemProto.bp_end', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=135,
  serialized_end=332,
)


_NODEMEMPROTO = _descriptor.Descriptor(
  name='NodeMemProto',
  full_name='mindspore.profiler.NodeMemProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='mindspore.profiler.NodeMemProto.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='mindspore.profiler.NodeMemProto.node_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_tensor_id', full_name='mindspore.profiler.NodeMemProto.input_tensor_id', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_tensor_id', full_name='mindspore.profiler.NodeMemProto.output_tensor_id', index=3,
      number=4, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workspace_tensor_id', full_name='mindspore.profiler.NodeMemProto.workspace_tensor_id', index=4,
      number=5, type=4, cpp_type=4, label=3,
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
  serialized_start=335,
  serialized_end=465,
)


_TENSORMEMPROTO = _descriptor.Descriptor(
  name='TensorMemProto',
  full_name='mindspore.profiler.TensorMemProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_id', full_name='mindspore.profiler.TensorMemProto.tensor_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='mindspore.profiler.TensorMemProto.size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='mindspore.profiler.TensorMemProto.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='life_start', full_name='mindspore.profiler.TensorMemProto.life_start', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='life_end', full_name='mindspore.profiler.TensorMemProto.life_end', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='life_long', full_name='mindspore.profiler.TensorMemProto.life_long', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=467,
  serialized_end=587,
)

_MEMORYPROTO.fields_by_name['graph_mem'].message_type = _GRAPHMEMPROTO
_GRAPHMEMPROTO.fields_by_name['node_mems'].message_type = _NODEMEMPROTO
_GRAPHMEMPROTO.fields_by_name['tensor_mems'].message_type = _TENSORMEMPROTO
DESCRIPTOR.message_types_by_name['MemoryProto'] = _MEMORYPROTO
DESCRIPTOR.message_types_by_name['GraphMemProto'] = _GRAPHMEMPROTO
DESCRIPTOR.message_types_by_name['NodeMemProto'] = _NODEMEMPROTO
DESCRIPTOR.message_types_by_name['TensorMemProto'] = _TENSORMEMPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MemoryProto = _reflection.GeneratedProtocolMessageType('MemoryProto', (_message.Message,), {
  'DESCRIPTOR' : _MEMORYPROTO,
  '__module__' : 'memory_profiling_pb2'
  # @@protoc_insertion_point(class_scope:mindspore.profiler.MemoryProto)
  })
_sym_db.RegisterMessage(MemoryProto)

GraphMemProto = _reflection.GeneratedProtocolMessageType('GraphMemProto', (_message.Message,), {
  'DESCRIPTOR' : _GRAPHMEMPROTO,
  '__module__' : 'memory_profiling_pb2'
  # @@protoc_insertion_point(class_scope:mindspore.profiler.GraphMemProto)
  })
_sym_db.RegisterMessage(GraphMemProto)

NodeMemProto = _reflection.GeneratedProtocolMessageType('NodeMemProto', (_message.Message,), {
  'DESCRIPTOR' : _NODEMEMPROTO,
  '__module__' : 'memory_profiling_pb2'
  # @@protoc_insertion_point(class_scope:mindspore.profiler.NodeMemProto)
  })
_sym_db.RegisterMessage(NodeMemProto)

TensorMemProto = _reflection.GeneratedProtocolMessageType('TensorMemProto', (_message.Message,), {
  'DESCRIPTOR' : _TENSORMEMPROTO,
  '__module__' : 'memory_profiling_pb2'
  # @@protoc_insertion_point(class_scope:mindspore.profiler.TensorMemProto)
  })
_sym_db.RegisterMessage(TensorMemProto)


# @@protoc_insertion_point(module_scope)
