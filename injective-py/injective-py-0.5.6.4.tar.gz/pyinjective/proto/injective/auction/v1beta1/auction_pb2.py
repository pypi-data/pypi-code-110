# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/auction/v1beta1/auction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/auction/v1beta1/auction.proto',
  package='injective.auction.v1beta1',
  syntax='proto3',
  serialized_options=b'ZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'injective/auction/v1beta1/auction.proto\x12\x19injective.auction.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"{\n\x06Params\x12\x16\n\x0e\x61uction_period\x18\x01 \x01(\x03\x12S\n\x1bmin_next_bid_increment_rate\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01\"s\n\x03\x42id\x12+\n\x06\x62idder\x18\x01 \x01(\tB\x1b\xea\xde\x1f\x06\x62idder\xf2\xde\x1f\ryaml:\"bidder\"\x12?\n\x06\x61mount\x18\x02 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00\"j\n\x08\x45ventBid\x12\x0e\n\x06\x62idder\x18\x01 \x01(\t\x12?\n\x06\x61mount\x18\x02 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00\x12\r\n\x05round\x18\x03 \x01(\x04\"t\n\x12\x45ventAuctionResult\x12\x0e\n\x06winner\x18\x01 \x01(\t\x12?\n\x06\x61mount\x18\x02 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00\x12\r\n\x05round\x18\x03 \x01(\x04\"\x9d\x01\n\x11\x45ventAuctionStart\x12\r\n\x05round\x18\x01 \x01(\x04\x12\x18\n\x10\x65nding_timestamp\x18\x02 \x01(\x03\x12_\n\nnew_basket\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsBOZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='injective.auction.v1beta1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auction_period', full_name='injective.auction.v1beta1.Params.auction_period', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_next_bid_increment_rate', full_name='injective.auction.v1beta1.Params.min_next_bid_increment_rate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=247,
)


_BID = _descriptor.Descriptor(
  name='Bid',
  full_name='injective.auction.v1beta1.Bid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bidder', full_name='injective.auction.v1beta1.Bid.bidder', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\006bidder\362\336\037\ryaml:\"bidder\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='injective.auction.v1beta1.Bid.amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=249,
  serialized_end=364,
)


_EVENTBID = _descriptor.Descriptor(
  name='EventBid',
  full_name='injective.auction.v1beta1.EventBid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bidder', full_name='injective.auction.v1beta1.EventBid.bidder', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='injective.auction.v1beta1.EventBid.amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='injective.auction.v1beta1.EventBid.round', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=366,
  serialized_end=472,
)


_EVENTAUCTIONRESULT = _descriptor.Descriptor(
  name='EventAuctionResult',
  full_name='injective.auction.v1beta1.EventAuctionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='winner', full_name='injective.auction.v1beta1.EventAuctionResult.winner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='injective.auction.v1beta1.EventAuctionResult.amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='injective.auction.v1beta1.EventAuctionResult.round', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=474,
  serialized_end=590,
)


_EVENTAUCTIONSTART = _descriptor.Descriptor(
  name='EventAuctionStart',
  full_name='injective.auction.v1beta1.EventAuctionStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='round', full_name='injective.auction.v1beta1.EventAuctionStart.round', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ending_timestamp', full_name='injective.auction.v1beta1.EventAuctionStart.ending_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_basket', full_name='injective.auction.v1beta1.EventAuctionStart.new_basket', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=593,
  serialized_end=750,
)

_EVENTAUCTIONSTART.fields_by_name['new_basket'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
DESCRIPTOR.message_types_by_name['Bid'] = _BID
DESCRIPTOR.message_types_by_name['EventBid'] = _EVENTBID
DESCRIPTOR.message_types_by_name['EventAuctionResult'] = _EVENTAUCTIONRESULT
DESCRIPTOR.message_types_by_name['EventAuctionStart'] = _EVENTAUCTIONSTART
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'injective.auction.v1beta1.auction_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)

Bid = _reflection.GeneratedProtocolMessageType('Bid', (_message.Message,), {
  'DESCRIPTOR' : _BID,
  '__module__' : 'injective.auction.v1beta1.auction_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.Bid)
  })
_sym_db.RegisterMessage(Bid)

EventBid = _reflection.GeneratedProtocolMessageType('EventBid', (_message.Message,), {
  'DESCRIPTOR' : _EVENTBID,
  '__module__' : 'injective.auction.v1beta1.auction_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.EventBid)
  })
_sym_db.RegisterMessage(EventBid)

EventAuctionResult = _reflection.GeneratedProtocolMessageType('EventAuctionResult', (_message.Message,), {
  'DESCRIPTOR' : _EVENTAUCTIONRESULT,
  '__module__' : 'injective.auction.v1beta1.auction_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.EventAuctionResult)
  })
_sym_db.RegisterMessage(EventAuctionResult)

EventAuctionStart = _reflection.GeneratedProtocolMessageType('EventAuctionStart', (_message.Message,), {
  'DESCRIPTOR' : _EVENTAUCTIONSTART,
  '__module__' : 'injective.auction.v1beta1.auction_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.EventAuctionStart)
  })
_sym_db.RegisterMessage(EventAuctionStart)


DESCRIPTOR._options = None
_PARAMS.fields_by_name['min_next_bid_increment_rate']._options = None
_PARAMS._options = None
_BID.fields_by_name['bidder']._options = None
_BID.fields_by_name['amount']._options = None
_EVENTBID.fields_by_name['amount']._options = None
_EVENTAUCTIONRESULT.fields_by_name['amount']._options = None
_EVENTAUCTIONSTART.fields_by_name['new_basket']._options = None
# @@protoc_insertion_point(module_scope)
