# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/util/json_format.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/protobuf/util/json_format.proto\x12\x11protobuf_unittest\"\x89\x01\n\x13TestFlagsAndStrings\x12\t\n\x01\x41\x18\x01 \x02(\x05\x12K\n\rrepeatedgroup\x18\x02 \x03(\n24.protobuf_unittest.TestFlagsAndStrings.RepeatedGroup\x1a\x1a\n\rRepeatedGroup\x12\t\n\x01\x66\x18\x03 \x02(\t\"!\n\x14TestBase64ByteArrays\x12\t\n\x01\x61\x18\x01 \x02(\x0c\"G\n\x12TestJavaScriptJSON\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\r\n\x05\x66inal\x18\x02 \x01(\x02\x12\n\n\x02in\x18\x03 \x01(\t\x12\x0b\n\x03Var\x18\x04 \x01(\t\"Q\n\x18TestJavaScriptOrderJSON1\x12\t\n\x01\x64\x18\x01 \x01(\x05\x12\t\n\x01\x63\x18\x02 \x01(\x05\x12\t\n\x01x\x18\x03 \x01(\x08\x12\t\n\x01\x62\x18\x04 \x01(\x05\x12\t\n\x01\x61\x18\x05 \x01(\x05\"\x89\x01\n\x18TestJavaScriptOrderJSON2\x12\t\n\x01\x64\x18\x01 \x01(\x05\x12\t\n\x01\x63\x18\x02 \x01(\x05\x12\t\n\x01x\x18\x03 \x01(\x08\x12\t\n\x01\x62\x18\x04 \x01(\x05\x12\t\n\x01\x61\x18\x05 \x01(\x05\x12\x36\n\x01z\x18\x06 \x03(\x0b\x32+.protobuf_unittest.TestJavaScriptOrderJSON1\"$\n\x0cTestLargeInt\x12\t\n\x01\x61\x18\x01 \x02(\x03\x12\t\n\x01\x62\x18\x02 \x02(\x04\"\xa0\x01\n\x0bTestNumbers\x12\x30\n\x01\x61\x18\x01 \x01(\x0e\x32%.protobuf_unittest.TestNumbers.MyType\x12\t\n\x01\x62\x18\x02 \x01(\x05\x12\t\n\x01\x63\x18\x03 \x01(\x02\x12\t\n\x01\x64\x18\x04 \x01(\x08\x12\t\n\x01\x65\x18\x05 \x01(\x01\x12\t\n\x01\x66\x18\x06 \x01(\r\"(\n\x06MyType\x12\x06\n\x02OK\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"T\n\rTestCamelCase\x12\x14\n\x0cnormal_field\x18\x01 \x01(\t\x12\x15\n\rCAPITAL_FIELD\x18\x02 \x01(\x05\x12\x16\n\x0e\x43\x61melCaseField\x18\x03 \x01(\x05\"|\n\x0bTestBoolMap\x12=\n\x08\x62ool_map\x18\x01 \x03(\x0b\x32+.protobuf_unittest.TestBoolMap.BoolMapEntry\x1a.\n\x0c\x42oolMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"O\n\rTestRecursion\x12\r\n\x05value\x18\x01 \x01(\x05\x12/\n\x05\x63hild\x18\x02 \x01(\x0b\x32 .protobuf_unittest.TestRecursion\"\x86\x01\n\rTestStringMap\x12\x43\n\nstring_map\x18\x01 \x03(\x0b\x32/.protobuf_unittest.TestStringMap.StringMapEntry\x1a\x30\n\x0eStringMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc4\x01\n\x14TestStringSerializer\x12\x15\n\rscalar_string\x18\x01 \x01(\t\x12\x17\n\x0frepeated_string\x18\x02 \x03(\t\x12J\n\nstring_map\x18\x03 \x03(\x0b\x32\x36.protobuf_unittest.TestStringSerializer.StringMapEntry\x1a\x30\n\x0eStringMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"$\n\x18TestMessageWithExtension*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"z\n\rTestExtension\x12\r\n\x05value\x18\x01 \x01(\t2Z\n\x03\x65xt\x12+.protobuf_unittest.TestMessageWithExtension\x18\x64 \x01(\x0b\x32 .protobuf_unittest.TestExtension\"Q\n\x14TestDefaultEnumValue\x12\x39\n\nenum_value\x18\x01 \x01(\x0e\x32\x1c.protobuf_unittest.EnumValue:\x07\x44\x45\x46\x41ULT*2\n\tEnumValue\x12\x0c\n\x08PROTOCOL\x10\x00\x12\n\n\x06\x42UFFER\x10\x01\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x02')

_ENUMVALUE = DESCRIPTOR.enum_types_by_name['EnumValue']
EnumValue = enum_type_wrapper.EnumTypeWrapper(_ENUMVALUE)
PROTOCOL = 0
BUFFER = 1
DEFAULT = 2


_TESTFLAGSANDSTRINGS = DESCRIPTOR.message_types_by_name['TestFlagsAndStrings']
_TESTFLAGSANDSTRINGS_REPEATEDGROUP = _TESTFLAGSANDSTRINGS.nested_types_by_name['RepeatedGroup']
_TESTBASE64BYTEARRAYS = DESCRIPTOR.message_types_by_name['TestBase64ByteArrays']
_TESTJAVASCRIPTJSON = DESCRIPTOR.message_types_by_name['TestJavaScriptJSON']
_TESTJAVASCRIPTORDERJSON1 = DESCRIPTOR.message_types_by_name['TestJavaScriptOrderJSON1']
_TESTJAVASCRIPTORDERJSON2 = DESCRIPTOR.message_types_by_name['TestJavaScriptOrderJSON2']
_TESTLARGEINT = DESCRIPTOR.message_types_by_name['TestLargeInt']
_TESTNUMBERS = DESCRIPTOR.message_types_by_name['TestNumbers']
_TESTCAMELCASE = DESCRIPTOR.message_types_by_name['TestCamelCase']
_TESTBOOLMAP = DESCRIPTOR.message_types_by_name['TestBoolMap']
_TESTBOOLMAP_BOOLMAPENTRY = _TESTBOOLMAP.nested_types_by_name['BoolMapEntry']
_TESTRECURSION = DESCRIPTOR.message_types_by_name['TestRecursion']
_TESTSTRINGMAP = DESCRIPTOR.message_types_by_name['TestStringMap']
_TESTSTRINGMAP_STRINGMAPENTRY = _TESTSTRINGMAP.nested_types_by_name['StringMapEntry']
_TESTSTRINGSERIALIZER = DESCRIPTOR.message_types_by_name['TestStringSerializer']
_TESTSTRINGSERIALIZER_STRINGMAPENTRY = _TESTSTRINGSERIALIZER.nested_types_by_name['StringMapEntry']
_TESTMESSAGEWITHEXTENSION = DESCRIPTOR.message_types_by_name['TestMessageWithExtension']
_TESTEXTENSION = DESCRIPTOR.message_types_by_name['TestExtension']
_TESTDEFAULTENUMVALUE = DESCRIPTOR.message_types_by_name['TestDefaultEnumValue']
_TESTNUMBERS_MYTYPE = _TESTNUMBERS.enum_types_by_name['MyType']
TestFlagsAndStrings = _reflection.GeneratedProtocolMessageType('TestFlagsAndStrings', (_message.Message,), {

  'RepeatedGroup' : _reflection.GeneratedProtocolMessageType('RepeatedGroup', (_message.Message,), {
    'DESCRIPTOR' : _TESTFLAGSANDSTRINGS_REPEATEDGROUP,
    '__module__' : 'google.protobuf.util.json_format_pb2'
    # @@protoc_insertion_point(class_scope:protobuf_unittest.TestFlagsAndStrings.RepeatedGroup)
    })
  ,
  'DESCRIPTOR' : _TESTFLAGSANDSTRINGS,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestFlagsAndStrings)
  })
_sym_db.RegisterMessage(TestFlagsAndStrings)
_sym_db.RegisterMessage(TestFlagsAndStrings.RepeatedGroup)

TestBase64ByteArrays = _reflection.GeneratedProtocolMessageType('TestBase64ByteArrays', (_message.Message,), {
  'DESCRIPTOR' : _TESTBASE64BYTEARRAYS,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestBase64ByteArrays)
  })
_sym_db.RegisterMessage(TestBase64ByteArrays)

TestJavaScriptJSON = _reflection.GeneratedProtocolMessageType('TestJavaScriptJSON', (_message.Message,), {
  'DESCRIPTOR' : _TESTJAVASCRIPTJSON,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestJavaScriptJSON)
  })
_sym_db.RegisterMessage(TestJavaScriptJSON)

TestJavaScriptOrderJSON1 = _reflection.GeneratedProtocolMessageType('TestJavaScriptOrderJSON1', (_message.Message,), {
  'DESCRIPTOR' : _TESTJAVASCRIPTORDERJSON1,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestJavaScriptOrderJSON1)
  })
_sym_db.RegisterMessage(TestJavaScriptOrderJSON1)

TestJavaScriptOrderJSON2 = _reflection.GeneratedProtocolMessageType('TestJavaScriptOrderJSON2', (_message.Message,), {
  'DESCRIPTOR' : _TESTJAVASCRIPTORDERJSON2,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestJavaScriptOrderJSON2)
  })
_sym_db.RegisterMessage(TestJavaScriptOrderJSON2)

TestLargeInt = _reflection.GeneratedProtocolMessageType('TestLargeInt', (_message.Message,), {
  'DESCRIPTOR' : _TESTLARGEINT,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestLargeInt)
  })
_sym_db.RegisterMessage(TestLargeInt)

TestNumbers = _reflection.GeneratedProtocolMessageType('TestNumbers', (_message.Message,), {
  'DESCRIPTOR' : _TESTNUMBERS,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestNumbers)
  })
_sym_db.RegisterMessage(TestNumbers)

TestCamelCase = _reflection.GeneratedProtocolMessageType('TestCamelCase', (_message.Message,), {
  'DESCRIPTOR' : _TESTCAMELCASE,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestCamelCase)
  })
_sym_db.RegisterMessage(TestCamelCase)

TestBoolMap = _reflection.GeneratedProtocolMessageType('TestBoolMap', (_message.Message,), {

  'BoolMapEntry' : _reflection.GeneratedProtocolMessageType('BoolMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _TESTBOOLMAP_BOOLMAPENTRY,
    '__module__' : 'google.protobuf.util.json_format_pb2'
    # @@protoc_insertion_point(class_scope:protobuf_unittest.TestBoolMap.BoolMapEntry)
    })
  ,
  'DESCRIPTOR' : _TESTBOOLMAP,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestBoolMap)
  })
_sym_db.RegisterMessage(TestBoolMap)
_sym_db.RegisterMessage(TestBoolMap.BoolMapEntry)

TestRecursion = _reflection.GeneratedProtocolMessageType('TestRecursion', (_message.Message,), {
  'DESCRIPTOR' : _TESTRECURSION,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestRecursion)
  })
_sym_db.RegisterMessage(TestRecursion)

TestStringMap = _reflection.GeneratedProtocolMessageType('TestStringMap', (_message.Message,), {

  'StringMapEntry' : _reflection.GeneratedProtocolMessageType('StringMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _TESTSTRINGMAP_STRINGMAPENTRY,
    '__module__' : 'google.protobuf.util.json_format_pb2'
    # @@protoc_insertion_point(class_scope:protobuf_unittest.TestStringMap.StringMapEntry)
    })
  ,
  'DESCRIPTOR' : _TESTSTRINGMAP,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestStringMap)
  })
_sym_db.RegisterMessage(TestStringMap)
_sym_db.RegisterMessage(TestStringMap.StringMapEntry)

TestStringSerializer = _reflection.GeneratedProtocolMessageType('TestStringSerializer', (_message.Message,), {

  'StringMapEntry' : _reflection.GeneratedProtocolMessageType('StringMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _TESTSTRINGSERIALIZER_STRINGMAPENTRY,
    '__module__' : 'google.protobuf.util.json_format_pb2'
    # @@protoc_insertion_point(class_scope:protobuf_unittest.TestStringSerializer.StringMapEntry)
    })
  ,
  'DESCRIPTOR' : _TESTSTRINGSERIALIZER,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestStringSerializer)
  })
_sym_db.RegisterMessage(TestStringSerializer)
_sym_db.RegisterMessage(TestStringSerializer.StringMapEntry)

TestMessageWithExtension = _reflection.GeneratedProtocolMessageType('TestMessageWithExtension', (_message.Message,), {
  'DESCRIPTOR' : _TESTMESSAGEWITHEXTENSION,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestMessageWithExtension)
  })
_sym_db.RegisterMessage(TestMessageWithExtension)

TestExtension = _reflection.GeneratedProtocolMessageType('TestExtension', (_message.Message,), {
  'DESCRIPTOR' : _TESTEXTENSION,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestExtension)
  })
_sym_db.RegisterMessage(TestExtension)

TestDefaultEnumValue = _reflection.GeneratedProtocolMessageType('TestDefaultEnumValue', (_message.Message,), {
  'DESCRIPTOR' : _TESTDEFAULTENUMVALUE,
  '__module__' : 'google.protobuf.util.json_format_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestDefaultEnumValue)
  })
_sym_db.RegisterMessage(TestDefaultEnumValue)

if _descriptor._USE_C_DESCRIPTORS == False:
  TestMessageWithExtension.RegisterExtension(_TESTEXTENSION.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _TESTBOOLMAP_BOOLMAPENTRY._options = None
  _TESTBOOLMAP_BOOLMAPENTRY._serialized_options = b'8\001'
  _TESTSTRINGMAP_STRINGMAPENTRY._options = None
  _TESTSTRINGMAP_STRINGMAPENTRY._serialized_options = b'8\001'
  _TESTSTRINGSERIALIZER_STRINGMAPENTRY._options = None
  _TESTSTRINGSERIALIZER_STRINGMAPENTRY._serialized_options = b'8\001'
  _ENUMVALUE._serialized_start=1607
  _ENUMVALUE._serialized_end=1657
  _TESTFLAGSANDSTRINGS._serialized_start=62
  _TESTFLAGSANDSTRINGS._serialized_end=199
  _TESTFLAGSANDSTRINGS_REPEATEDGROUP._serialized_start=173
  _TESTFLAGSANDSTRINGS_REPEATEDGROUP._serialized_end=199
  _TESTBASE64BYTEARRAYS._serialized_start=201
  _TESTBASE64BYTEARRAYS._serialized_end=234
  _TESTJAVASCRIPTJSON._serialized_start=236
  _TESTJAVASCRIPTJSON._serialized_end=307
  _TESTJAVASCRIPTORDERJSON1._serialized_start=309
  _TESTJAVASCRIPTORDERJSON1._serialized_end=390
  _TESTJAVASCRIPTORDERJSON2._serialized_start=393
  _TESTJAVASCRIPTORDERJSON2._serialized_end=530
  _TESTLARGEINT._serialized_start=532
  _TESTLARGEINT._serialized_end=568
  _TESTNUMBERS._serialized_start=571
  _TESTNUMBERS._serialized_end=731
  _TESTNUMBERS_MYTYPE._serialized_start=691
  _TESTNUMBERS_MYTYPE._serialized_end=731
  _TESTCAMELCASE._serialized_start=733
  _TESTCAMELCASE._serialized_end=817
  _TESTBOOLMAP._serialized_start=819
  _TESTBOOLMAP._serialized_end=943
  _TESTBOOLMAP_BOOLMAPENTRY._serialized_start=897
  _TESTBOOLMAP_BOOLMAPENTRY._serialized_end=943
  _TESTRECURSION._serialized_start=945
  _TESTRECURSION._serialized_end=1024
  _TESTSTRINGMAP._serialized_start=1027
  _TESTSTRINGMAP._serialized_end=1161
  _TESTSTRINGMAP_STRINGMAPENTRY._serialized_start=1113
  _TESTSTRINGMAP_STRINGMAPENTRY._serialized_end=1161
  _TESTSTRINGSERIALIZER._serialized_start=1164
  _TESTSTRINGSERIALIZER._serialized_end=1360
  _TESTSTRINGSERIALIZER_STRINGMAPENTRY._serialized_start=1113
  _TESTSTRINGSERIALIZER_STRINGMAPENTRY._serialized_end=1161
  _TESTMESSAGEWITHEXTENSION._serialized_start=1362
  _TESTMESSAGEWITHEXTENSION._serialized_end=1398
  _TESTEXTENSION._serialized_start=1400
  _TESTEXTENSION._serialized_end=1522
  _TESTDEFAULTENUMVALUE._serialized_start=1524
  _TESTDEFAULTENUMVALUE._serialized_end=1605
# @@protoc_insertion_point(module_scope)
