# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lte_registration.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import lte_pb2 as lte__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lte_registration.proto',
  package='com.airhopcomm.eson.lte.registration.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16lte_registration.proto\x12\'com.airhopcomm.eson.lte.registration.v1\x1a\tlte.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x12\n\x10SubscribeRequest\"b\n\x07Message\x12P\n\x0cregister_cmd\x18\x01 \x01(\x0b\x32\x38.com.airhopcomm.eson.lte.registration.v1.RegisterCommandH\x00\x42\x05\n\x03msg\"\x11\n\x0fRegisterCommand\"Q\n\x10RegisterResponse\x12\x0c\n\x04\x65\x63gi\x18\x01 \x01(\x06\x12/\n\terror_msg\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"!\n\x11UnregisterRequest\x12\x0c\n\x04\x65\x63gi\x18\x01 \x01(\x06\"\x14\n\x12UnregisterResponse\"[\n\x12\x41\x64\x64NeighborRequest\x12\x0c\n\x04\x65\x63gi\x18\x01 \x01(\x06\x12\x37\n\tneighbors\x18\x02 \x03(\x0b\x32$.com.airhopcomm.eson.lte.v1.Neighbor\"\x15\n\x13\x41\x64\x64NeighborResponse\"=\n\x15RemoveNeighborRequest\x12\x0c\n\x04\x65\x63gi\x18\x01 \x01(\x06\x12\x16\n\x0eneighbor_ecgis\x18\x02 \x03(\x06\"\x18\n\x16RemoveNeighborResponse2\xaf\x05\n\x13RegistrationService\x12|\n\tSubscribe\x12\x39.com.airhopcomm.eson.lte.registration.v1.SubscribeRequest\x1a\x30.com.airhopcomm.eson.lte.registration.v1.Message\"\x00\x30\x01\x12m\n\x08Register\x12 .com.airhopcomm.eson.lte.v1.Cell\x1a\x39.com.airhopcomm.eson.lte.registration.v1.RegisterResponse\"\x00(\x01\x30\x01\x12\x87\x01\n\nUnregister\x12:.com.airhopcomm.eson.lte.registration.v1.UnregisterRequest\x1a;.com.airhopcomm.eson.lte.registration.v1.UnregisterResponse\"\x00\x12\x8a\x01\n\x0b\x41\x64\x64Neighbor\x12;.com.airhopcomm.eson.lte.registration.v1.AddNeighborRequest\x1a<.com.airhopcomm.eson.lte.registration.v1.AddNeighborResponse\"\x00\x12\x93\x01\n\x0eRemoveNeighbor\x12>.com.airhopcomm.eson.lte.registration.v1.RemoveNeighborRequest\x1a?.com.airhopcomm.eson.lte.registration.v1.RemoveNeighborResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[lte__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='com.airhopcomm.eson.lte.registration.v1.SubscribeRequest',
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
  serialized_start=110,
  serialized_end=128,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='com.airhopcomm.eson.lte.registration.v1.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='register_cmd', full_name='com.airhopcomm.eson.lte.registration.v1.Message.register_cmd', index=0,
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
    _descriptor.OneofDescriptor(
      name='msg', full_name='com.airhopcomm.eson.lte.registration.v1.Message.msg',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=130,
  serialized_end=228,
)


_REGISTERCOMMAND = _descriptor.Descriptor(
  name='RegisterCommand',
  full_name='com.airhopcomm.eson.lte.registration.v1.RegisterCommand',
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
  serialized_start=230,
  serialized_end=247,
)


_REGISTERRESPONSE = _descriptor.Descriptor(
  name='RegisterResponse',
  full_name='com.airhopcomm.eson.lte.registration.v1.RegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ecgi', full_name='com.airhopcomm.eson.lte.registration.v1.RegisterResponse.ecgi', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='com.airhopcomm.eson.lte.registration.v1.RegisterResponse.error_msg', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=249,
  serialized_end=330,
)


_UNREGISTERREQUEST = _descriptor.Descriptor(
  name='UnregisterRequest',
  full_name='com.airhopcomm.eson.lte.registration.v1.UnregisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ecgi', full_name='com.airhopcomm.eson.lte.registration.v1.UnregisterRequest.ecgi', index=0,
      number=1, type=6, cpp_type=4, label=1,
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
  serialized_start=332,
  serialized_end=365,
)


_UNREGISTERRESPONSE = _descriptor.Descriptor(
  name='UnregisterResponse',
  full_name='com.airhopcomm.eson.lte.registration.v1.UnregisterResponse',
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
  serialized_start=367,
  serialized_end=387,
)


_ADDNEIGHBORREQUEST = _descriptor.Descriptor(
  name='AddNeighborRequest',
  full_name='com.airhopcomm.eson.lte.registration.v1.AddNeighborRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ecgi', full_name='com.airhopcomm.eson.lte.registration.v1.AddNeighborRequest.ecgi', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='neighbors', full_name='com.airhopcomm.eson.lte.registration.v1.AddNeighborRequest.neighbors', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=389,
  serialized_end=480,
)


_ADDNEIGHBORRESPONSE = _descriptor.Descriptor(
  name='AddNeighborResponse',
  full_name='com.airhopcomm.eson.lte.registration.v1.AddNeighborResponse',
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
  serialized_start=482,
  serialized_end=503,
)


_REMOVENEIGHBORREQUEST = _descriptor.Descriptor(
  name='RemoveNeighborRequest',
  full_name='com.airhopcomm.eson.lte.registration.v1.RemoveNeighborRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ecgi', full_name='com.airhopcomm.eson.lte.registration.v1.RemoveNeighborRequest.ecgi', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='neighbor_ecgis', full_name='com.airhopcomm.eson.lte.registration.v1.RemoveNeighborRequest.neighbor_ecgis', index=1,
      number=2, type=6, cpp_type=4, label=3,
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
  serialized_start=505,
  serialized_end=566,
)


_REMOVENEIGHBORRESPONSE = _descriptor.Descriptor(
  name='RemoveNeighborResponse',
  full_name='com.airhopcomm.eson.lte.registration.v1.RemoveNeighborResponse',
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
  serialized_start=568,
  serialized_end=592,
)

_MESSAGE.fields_by_name['register_cmd'].message_type = _REGISTERCOMMAND
_MESSAGE.oneofs_by_name['msg'].fields.append(
  _MESSAGE.fields_by_name['register_cmd'])
_MESSAGE.fields_by_name['register_cmd'].containing_oneof = _MESSAGE.oneofs_by_name['msg']
_REGISTERRESPONSE.fields_by_name['error_msg'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADDNEIGHBORREQUEST.fields_by_name['neighbors'].message_type = lte__pb2._NEIGHBOR
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['RegisterCommand'] = _REGISTERCOMMAND
DESCRIPTOR.message_types_by_name['RegisterResponse'] = _REGISTERRESPONSE
DESCRIPTOR.message_types_by_name['UnregisterRequest'] = _UNREGISTERREQUEST
DESCRIPTOR.message_types_by_name['UnregisterResponse'] = _UNREGISTERRESPONSE
DESCRIPTOR.message_types_by_name['AddNeighborRequest'] = _ADDNEIGHBORREQUEST
DESCRIPTOR.message_types_by_name['AddNeighborResponse'] = _ADDNEIGHBORRESPONSE
DESCRIPTOR.message_types_by_name['RemoveNeighborRequest'] = _REMOVENEIGHBORREQUEST
DESCRIPTOR.message_types_by_name['RemoveNeighborResponse'] = _REMOVENEIGHBORRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'lte_registration_pb2'
  # @@protoc_insertion_point(class_scope:com.airhopcomm.eson.lte.registration.v1.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'lte_registration_pb2'
  # @@protoc_insertion_point(class_scope:com.airhopcomm.eson.lte.registration.v1.Message)
  })
_sym_db.RegisterMessage(Message)

RegisterCommand = _reflection.GeneratedProtocolMessageType('RegisterCommand', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERCOMMAND,
  '__module__' : 'lte_registration_pb2'
  # @@protoc_insertion_point(class_scope:com.airhopcomm.eson.lte.registration.v1.RegisterCommand)
  })
_sym_db.RegisterMessage(RegisterCommand)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONSE,
  '__module__' : 'lte_registration_pb2'
  # @@protoc_insertion_point(class_scope:com.airhopcomm.eson.lte.registration.v1.RegisterResponse)
  })
_sym_db.RegisterMessage(RegisterResponse)

UnregisterRequest = _reflection.GeneratedProtocolMessageType('UnregisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNREGISTERREQUEST,
  '__module__' : 'lte_registration_pb2'
  # @@protoc_insertion_point(class_scope:com.airhopcomm.eson.lte.registration.v1.UnregisterRequest)
  })
_sym_db.RegisterMessage(UnregisterRequest)

UnregisterResponse = _reflection.GeneratedProtocolMessageType('UnregisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNREGISTERRESPONSE,
  '__module__' : 'lte_registration_pb2'
  # @@protoc_insertion_point(class_scope:com.airhopcomm.eson.lte.registration.v1.UnregisterResponse)
  })
_sym_db.RegisterMessage(UnregisterResponse)

AddNeighborRequest = _reflection.GeneratedProtocolMessageType('AddNeighborRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDNEIGHBORREQUEST,
  '__module__' : 'lte_registration_pb2'
  # @@protoc_insertion_point(class_scope:com.airhopcomm.eson.lte.registration.v1.AddNeighborRequest)
  })
_sym_db.RegisterMessage(AddNeighborRequest)

AddNeighborResponse = _reflection.GeneratedProtocolMessageType('AddNeighborResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDNEIGHBORRESPONSE,
  '__module__' : 'lte_registration_pb2'
  # @@protoc_insertion_point(class_scope:com.airhopcomm.eson.lte.registration.v1.AddNeighborResponse)
  })
_sym_db.RegisterMessage(AddNeighborResponse)

RemoveNeighborRequest = _reflection.GeneratedProtocolMessageType('RemoveNeighborRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVENEIGHBORREQUEST,
  '__module__' : 'lte_registration_pb2'
  # @@protoc_insertion_point(class_scope:com.airhopcomm.eson.lte.registration.v1.RemoveNeighborRequest)
  })
_sym_db.RegisterMessage(RemoveNeighborRequest)

RemoveNeighborResponse = _reflection.GeneratedProtocolMessageType('RemoveNeighborResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVENEIGHBORRESPONSE,
  '__module__' : 'lte_registration_pb2'
  # @@protoc_insertion_point(class_scope:com.airhopcomm.eson.lte.registration.v1.RemoveNeighborResponse)
  })
_sym_db.RegisterMessage(RemoveNeighborResponse)



_REGISTRATIONSERVICE = _descriptor.ServiceDescriptor(
  name='RegistrationService',
  full_name='com.airhopcomm.eson.lte.registration.v1.RegistrationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=595,
  serialized_end=1282,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='com.airhopcomm.eson.lte.registration.v1.RegistrationService.Subscribe',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='com.airhopcomm.eson.lte.registration.v1.RegistrationService.Register',
    index=1,
    containing_service=None,
    input_type=lte__pb2._CELL,
    output_type=_REGISTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Unregister',
    full_name='com.airhopcomm.eson.lte.registration.v1.RegistrationService.Unregister',
    index=2,
    containing_service=None,
    input_type=_UNREGISTERREQUEST,
    output_type=_UNREGISTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddNeighbor',
    full_name='com.airhopcomm.eson.lte.registration.v1.RegistrationService.AddNeighbor',
    index=3,
    containing_service=None,
    input_type=_ADDNEIGHBORREQUEST,
    output_type=_ADDNEIGHBORRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveNeighbor',
    full_name='com.airhopcomm.eson.lte.registration.v1.RegistrationService.RemoveNeighbor',
    index=4,
    containing_service=None,
    input_type=_REMOVENEIGHBORREQUEST,
    output_type=_REMOVENEIGHBORRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REGISTRATIONSERVICE)

DESCRIPTOR.services_by_name['RegistrationService'] = _REGISTRATIONSERVICE

# @@protoc_insertion_point(module_scope)
