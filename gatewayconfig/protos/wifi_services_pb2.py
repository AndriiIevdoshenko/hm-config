# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wifi_services.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wifi_services.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13wifi_services.proto\"$\n\x10wifi_services_v1\x12\x10\n\x08services\x18\x01 \x03(\tb\x06proto3'
)




_WIFI_SERVICES_V1 = _descriptor.Descriptor(
  name='wifi_services_v1',
  full_name='wifi_services_v1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='wifi_services_v1.services', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=23,
  serialized_end=59,
)

DESCRIPTOR.message_types_by_name['wifi_services_v1'] = _WIFI_SERVICES_V1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

wifi_services_v1 = _reflection.GeneratedProtocolMessageType('wifi_services_v1', (_message.Message,), {
  'DESCRIPTOR' : _WIFI_SERVICES_V1,
  '__module__' : 'wifi_services_pb2'
  # @@protoc_insertion_point(class_scope:wifi_services_v1)
  })
_sym_db.RegisterMessage(wifi_services_v1)


# @@protoc_insertion_point(module_scope)
