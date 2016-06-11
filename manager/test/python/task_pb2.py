# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='blaze',
  serialized_pb='\n\ntask.proto\x12\x05\x62laze\"\xe8\x01\n\x07\x44\x61taMsg\x12\x14\n\x0cpartition_id\x18\x01 \x01(\x03\x12\x0e\n\x06\x63\x61\x63hed\x18\x02 \x01(\x08\x12\x0f\n\x07sampled\x18\x03 \x01(\x08\x12\x16\n\x0e\x65lement_length\x18\x04 \x01(\x05\x12\x14\n\x0c\x65lement_size\x18\x05 \x01(\x05\x12\x14\n\x0cnum_elements\x18\x06 \x01(\x05\x12\x14\n\x0cscalar_value\x18\x07 \x01(\x03\x12\x11\n\tfile_path\x18\x08 \x01(\t\x12\x11\n\tfile_size\x18\t \x01(\x03\x12\x13\n\x0b\x66ile_offset\x18\n \x01(\x03\x12\x11\n\tmask_path\x18\x0b \x01(\t\"\x8e\x01\n\x07TaskMsg\x12\x1c\n\x04type\x18\x01 \x02(\x0e\x32\x0e.blaze.MsgType\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63\x63_id\x18\x03 \x01(\t\x12\x1c\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x0e.blaze.DataMsg\x12\x1a\n\x03\x61\x63\x63\x18\x05 \x01(\x0b\x32\r.blaze.AccMsg\x12\x0b\n\x03msg\x18\x06 \x01(\t\"\x8f\x01\n\x06\x41\x63\x63Msg\x12\x0e\n\x06\x61\x63\x63_id\x18\x01 \x02(\t\x12\x13\n\x0bplatform_id\x18\x02 \x02(\t\x12\x11\n\ttask_impl\x18\x03 \x01(\x0c\x12%\n\x05param\x18\x04 \x03(\x0b\x32\x16.blaze.AccMsg.KeyValue\x1a&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\x0c*\xa1\x01\n\x07MsgType\x12\x0e\n\nACCREQUEST\x10\x00\x12\x0c\n\x08\x41\x43\x43GRANT\x10\x01\x12\r\n\tACCREJECT\x10\x02\x12\r\n\tACCFINISH\x10\x03\x12\x0b\n\x07\x41\x43\x43\x44\x41TA\x10\x04\x12\x0e\n\nACCFAILURE\x10\x05\x12\x10\n\x0c\x41\x43\x43\x42ROADCAST\x10\x06\x12\x0b\n\x07\x41\x43\x43TERM\x10\x07\x12\x0f\n\x0b\x41\x43\x43REGISTER\x10\x08\x12\r\n\tACCDELETE\x10\tB$\n\x16org.apache.spark.blazeB\nAccMessage')

_MSGTYPE = _descriptor.EnumDescriptor(
  name='MsgType',
  full_name='blaze.MsgType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACCREQUEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCGRANT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCREJECT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCFINISH', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCDATA', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCFAILURE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCBROADCAST', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCTERM', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCREGISTER', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCDELETE', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=548,
  serialized_end=709,
)

MsgType = enum_type_wrapper.EnumTypeWrapper(_MSGTYPE)
ACCREQUEST = 0
ACCGRANT = 1
ACCREJECT = 2
ACCFINISH = 3
ACCDATA = 4
ACCFAILURE = 5
ACCBROADCAST = 6
ACCTERM = 7
ACCREGISTER = 8
ACCDELETE = 9



_DATAMSG = _descriptor.Descriptor(
  name='DataMsg',
  full_name='blaze.DataMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partition_id', full_name='blaze.DataMsg.partition_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cached', full_name='blaze.DataMsg.cached', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sampled', full_name='blaze.DataMsg.sampled', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='element_length', full_name='blaze.DataMsg.element_length', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='element_size', full_name='blaze.DataMsg.element_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_elements', full_name='blaze.DataMsg.num_elements', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scalar_value', full_name='blaze.DataMsg.scalar_value', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='blaze.DataMsg.file_path', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='blaze.DataMsg.file_size', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_offset', full_name='blaze.DataMsg.file_offset', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_path', full_name='blaze.DataMsg.mask_path', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=22,
  serialized_end=254,
)


_TASKMSG = _descriptor.Descriptor(
  name='TaskMsg',
  full_name='blaze.TaskMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='blaze.TaskMsg.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='blaze.TaskMsg.app_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acc_id', full_name='blaze.TaskMsg.acc_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='blaze.TaskMsg.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acc', full_name='blaze.TaskMsg.acc', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='blaze.TaskMsg.msg', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=257,
  serialized_end=399,
)


_ACCMSG_KEYVALUE = _descriptor.Descriptor(
  name='KeyValue',
  full_name='blaze.AccMsg.KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='blaze.AccMsg.KeyValue.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='blaze.AccMsg.KeyValue.value', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=507,
  serialized_end=545,
)

_ACCMSG = _descriptor.Descriptor(
  name='AccMsg',
  full_name='blaze.AccMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acc_id', full_name='blaze.AccMsg.acc_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform_id', full_name='blaze.AccMsg.platform_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_impl', full_name='blaze.AccMsg.task_impl', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param', full_name='blaze.AccMsg.param', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ACCMSG_KEYVALUE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=402,
  serialized_end=545,
)

_TASKMSG.fields_by_name['type'].enum_type = _MSGTYPE
_TASKMSG.fields_by_name['data'].message_type = _DATAMSG
_TASKMSG.fields_by_name['acc'].message_type = _ACCMSG
_ACCMSG_KEYVALUE.containing_type = _ACCMSG;
_ACCMSG.fields_by_name['param'].message_type = _ACCMSG_KEYVALUE
DESCRIPTOR.message_types_by_name['DataMsg'] = _DATAMSG
DESCRIPTOR.message_types_by_name['TaskMsg'] = _TASKMSG
DESCRIPTOR.message_types_by_name['AccMsg'] = _ACCMSG

class DataMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATAMSG

  # @@protoc_insertion_point(class_scope:blaze.DataMsg)

class TaskMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKMSG

  # @@protoc_insertion_point(class_scope:blaze.TaskMsg)

class AccMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class KeyValue(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ACCMSG_KEYVALUE

    # @@protoc_insertion_point(class_scope:blaze.AccMsg.KeyValue)
  DESCRIPTOR = _ACCMSG

  # @@protoc_insertion_point(class_scope:blaze.AccMsg)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\026org.apache.spark.blazeB\nAccMessage')
# @@protoc_insertion_point(module_scope)
