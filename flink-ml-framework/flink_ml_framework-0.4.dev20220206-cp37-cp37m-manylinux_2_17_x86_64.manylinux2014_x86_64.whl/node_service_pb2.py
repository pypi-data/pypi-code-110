# -*- coding: utf-8 -*-

#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import node_pb2 as node__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='node_service.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n org.flinkextended.flink.ml.protoB\021NodeServiceProtosP\001'),
  serialized_pb=_b('\n\x12node_service.proto\x1a\nnode.proto2\xd1\x02\n\x0bNodeService\x12\x32\n\x0bGetNodeSpec\x12\x10.NodeSpecRequest\x1a\x11.NodeSpecResponse\x12\x38\n\x0bNodeRestart\x12\x13.NodeRestartRequest\x1a\x14.NodeRestartResponse\x12/\n\x08NodeStop\x12\x10.NodeStopRequest\x1a\x11.NodeStopResponse\x12/\n\nGetContext\x12\x0f.ContextRequest\x1a\x10.ContextResponse\x12<\n\x0fGetFinishWorker\x12\x12.NodeSimpleRequest\x1a\x15.FinishWorkerResponse\x12\x34\n\tFinishJob\x12\x12.NodeSimpleRequest\x1a\x13.NodeSimpleResponseB7\n org.flinkextended.flink.ml.protoB\x11NodeServiceProtosP\x01\x62\x06proto3')
  ,
  dependencies=[node__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_NODESERVICE = _descriptor.ServiceDescriptor(
  name='NodeService',
  full_name='NodeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=35,
  serialized_end=372,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetNodeSpec',
    full_name='NodeService.GetNodeSpec',
    index=0,
    containing_service=None,
    input_type=node__pb2._NODESPECREQUEST,
    output_type=node__pb2._NODESPECRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NodeRestart',
    full_name='NodeService.NodeRestart',
    index=1,
    containing_service=None,
    input_type=node__pb2._NODERESTARTREQUEST,
    output_type=node__pb2._NODERESTARTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NodeStop',
    full_name='NodeService.NodeStop',
    index=2,
    containing_service=None,
    input_type=node__pb2._NODESTOPREQUEST,
    output_type=node__pb2._NODESTOPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetContext',
    full_name='NodeService.GetContext',
    index=3,
    containing_service=None,
    input_type=node__pb2._CONTEXTREQUEST,
    output_type=node__pb2._CONTEXTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFinishWorker',
    full_name='NodeService.GetFinishWorker',
    index=4,
    containing_service=None,
    input_type=node__pb2._NODESIMPLEREQUEST,
    output_type=node__pb2._FINISHWORKERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FinishJob',
    full_name='NodeService.FinishJob',
    index=5,
    containing_service=None,
    input_type=node__pb2._NODESIMPLEREQUEST,
    output_type=node__pb2._NODESIMPLERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NODESERVICE)

DESCRIPTOR.services_by_name['NodeService'] = _NODESERVICE

# @@protoc_insertion_point(module_scope)
