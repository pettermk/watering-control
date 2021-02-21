# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: web/grpc/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='web/grpc/service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16web/grpc/service.proto\x1a\x1cgoogle/protobuf/struct.proto\"4\n\x05Input\x12+\n\nproperties\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"5\n\x06Output\x12+\n\nproperties\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"9\n\nController\x12+\n\nproperties\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"`\n\rConfiguration\x12\x15\n\x05input\x18\x01 \x01(\x0b\x32\x06.Input\x12\x17\n\x06output\x18\x02 \x01(\x0b\x32\x07.Output\x12\x1f\n\ncontroller\x18\x03 \x01(\x0b\x32\x0b.Controller\"8\n\x0e\x43onfigurations\x12&\n\x0e\x63onfigurations\x18\x01 \x03(\x0b\x32\x0e.Configuration\"\x14\n\x06Status\x12\n\n\x02ok\x18\x02 \x01(\x08\"&\n\x05Value\x12\x0e\n\x06\x64\x65vice\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\x02\" \n\x06Values\x12\x16\n\x06values\x18\x05 \x03(\x0b\x32\x06.Value2g\n\x0fWaterController\x12,\n\x0e\x41\x64\x64\x43ontrollers\x12\x0f.Configurations\x1a\x07.Status\"\x00\x12&\n\tGetValues\x12\x0e.Configuration\x1a\x07.Values\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='properties', full_name='Input.properties', index=0,
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
  serialized_start=56,
  serialized_end=108,
)


_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='properties', full_name='Output.properties', index=0,
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
  serialized_start=110,
  serialized_end=163,
)


_CONTROLLER = _descriptor.Descriptor(
  name='Controller',
  full_name='Controller',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='properties', full_name='Controller.properties', index=0,
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
  serialized_start=165,
  serialized_end=222,
)


_CONFIGURATION = _descriptor.Descriptor(
  name='Configuration',
  full_name='Configuration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='Configuration.input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output', full_name='Configuration.output', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='controller', full_name='Configuration.controller', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=224,
  serialized_end=320,
)


_CONFIGURATIONS = _descriptor.Descriptor(
  name='Configurations',
  full_name='Configurations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='configurations', full_name='Configurations.configurations', index=0,
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
  serialized_start=322,
  serialized_end=378,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok', full_name='Status.ok', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=380,
  serialized_end=400,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='Value.device', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Value.value', index=1,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=402,
  serialized_end=440,
)


_VALUES = _descriptor.Descriptor(
  name='Values',
  full_name='Values',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='Values.values', index=0,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=442,
  serialized_end=474,
)

_INPUT.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_OUTPUT.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CONTROLLER.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CONFIGURATION.fields_by_name['input'].message_type = _INPUT
_CONFIGURATION.fields_by_name['output'].message_type = _OUTPUT
_CONFIGURATION.fields_by_name['controller'].message_type = _CONTROLLER
_CONFIGURATIONS.fields_by_name['configurations'].message_type = _CONFIGURATION
_VALUES.fields_by_name['values'].message_type = _VALUE
DESCRIPTOR.message_types_by_name['Input'] = _INPUT
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['Controller'] = _CONTROLLER
DESCRIPTOR.message_types_by_name['Configuration'] = _CONFIGURATION
DESCRIPTOR.message_types_by_name['Configurations'] = _CONFIGURATIONS
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['Values'] = _VALUES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'web.grpc.service_pb2'
  # @@protoc_insertion_point(class_scope:Input)
  })
_sym_db.RegisterMessage(Input)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'web.grpc.service_pb2'
  # @@protoc_insertion_point(class_scope:Output)
  })
_sym_db.RegisterMessage(Output)

Controller = _reflection.GeneratedProtocolMessageType('Controller', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLLER,
  '__module__' : 'web.grpc.service_pb2'
  # @@protoc_insertion_point(class_scope:Controller)
  })
_sym_db.RegisterMessage(Controller)

Configuration = _reflection.GeneratedProtocolMessageType('Configuration', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATION,
  '__module__' : 'web.grpc.service_pb2'
  # @@protoc_insertion_point(class_scope:Configuration)
  })
_sym_db.RegisterMessage(Configuration)

Configurations = _reflection.GeneratedProtocolMessageType('Configurations', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONS,
  '__module__' : 'web.grpc.service_pb2'
  # @@protoc_insertion_point(class_scope:Configurations)
  })
_sym_db.RegisterMessage(Configurations)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'web.grpc.service_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  })
_sym_db.RegisterMessage(Status)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'web.grpc.service_pb2'
  # @@protoc_insertion_point(class_scope:Value)
  })
_sym_db.RegisterMessage(Value)

Values = _reflection.GeneratedProtocolMessageType('Values', (_message.Message,), {
  'DESCRIPTOR' : _VALUES,
  '__module__' : 'web.grpc.service_pb2'
  # @@protoc_insertion_point(class_scope:Values)
  })
_sym_db.RegisterMessage(Values)



_WATERCONTROLLER = _descriptor.ServiceDescriptor(
  name='WaterController',
  full_name='WaterController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=476,
  serialized_end=579,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddControllers',
    full_name='WaterController.AddControllers',
    index=0,
    containing_service=None,
    input_type=_CONFIGURATIONS,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetValues',
    full_name='WaterController.GetValues',
    index=1,
    containing_service=None,
    input_type=_CONFIGURATION,
    output_type=_VALUES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WATERCONTROLLER)

DESCRIPTOR.services_by_name['WaterController'] = _WATERCONTROLLER

# @@protoc_insertion_point(module_scope)
