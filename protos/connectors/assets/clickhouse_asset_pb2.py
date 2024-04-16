# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/connectors/assets/clickhouse_asset.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos.connectors import connector_pb2 as protos_dot_connectors_dot_connector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/protos/connectors/assets/clickhouse_asset.proto\x12\x18protos.connectors.assets\x1a\x1egoogle/protobuf/wrappers.proto\x1a!protos/connectors/connector.proto\"\xc9\x01\n\x0f\x43lickhouseAsset\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x38\n\x0e\x63onnector_type\x18\x02 \x01(\x0e\x32 .protos.connectors.ConnectorType\x12;\n\x04type\x18\x03 \x01(\x0e\x32-.protos.connectors.ConnectorMetadataModelType\x12\x0b\n\x03uid\x18\x04 \x01(\t\x12\x14\n\x0clast_updated\x18\x05 \x01(\x04\x12\x10\n\x08metadata\x18\x06 \x01(\t\"\xf2\t\n\x1c\x43lickhouseDatabaseAssetModel\x12.\n\x08\x64\x61tabase\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12V\n\x06tables\x18\x02 \x03(\x0b\x32\x46.protos.connectors.assets.ClickhouseDatabaseAssetModel.ClickhouseTable\x1a\xc9\x08\n\x0f\x43lickhouseTable\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x65ngine\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rpartition_key\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0epartition_type\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14partition_expression\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08order_by\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tsample_by\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bprimary_key\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06sample\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x03ttl\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08settings\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10timestamp_column\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12h\n\x07\x63olumns\x18\r \x03(\x0b\x32W.protos.connectors.assets.ClickhouseDatabaseAssetModel.ClickhouseTable.ClickhouseColumn\x1a\xf5\x02\n\x10\x43lickhouseColumn\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04type\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07\x63omment\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x64\x65\x66\x61ult_type\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0ettl_expression\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x63odec_expression\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12\x64\x65\x66\x61ult_expression\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"3\n\x1e\x43lickhouseDatabaseAssetOptions\x12\x11\n\tdatabases\x18\x01 \x03(\t\"\xad\x02\n\x14\x43lickhouseAssetModel\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x38\n\x0e\x63onnector_type\x18\x02 \x01(\x0e\x32 .protos.connectors.ConnectorType\x12;\n\x04type\x18\x03 \x01(\x0e\x32-.protos.connectors.ConnectorMetadataModelType\x12\x14\n\x0clast_updated\x18\x04 \x01(\x10\x12U\n\x13\x63lickhouse_database\x18\x05 \x01(\x0b\x32\x36.protos.connectors.assets.ClickhouseDatabaseAssetModelH\x00\x42\x07\n\x05\x61sset\"R\n\x10\x43lickhouseAssets\x12>\n\x06\x61ssets\x18\x01 \x03(\x0b\x32..protos.connectors.assets.ClickhouseAssetModelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.connectors.assets.clickhouse_asset_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLICKHOUSEASSET._serialized_start=145
  _CLICKHOUSEASSET._serialized_end=346
  _CLICKHOUSEDATABASEASSETMODEL._serialized_start=349
  _CLICKHOUSEDATABASEASSETMODEL._serialized_end=1615
  _CLICKHOUSEDATABASEASSETMODEL_CLICKHOUSETABLE._serialized_start=518
  _CLICKHOUSEDATABASEASSETMODEL_CLICKHOUSETABLE._serialized_end=1615
  _CLICKHOUSEDATABASEASSETMODEL_CLICKHOUSETABLE_CLICKHOUSECOLUMN._serialized_start=1242
  _CLICKHOUSEDATABASEASSETMODEL_CLICKHOUSETABLE_CLICKHOUSECOLUMN._serialized_end=1615
  _CLICKHOUSEDATABASEASSETOPTIONS._serialized_start=1617
  _CLICKHOUSEDATABASEASSETOPTIONS._serialized_end=1668
  _CLICKHOUSEASSETMODEL._serialized_start=1671
  _CLICKHOUSEASSETMODEL._serialized_end=1972
  _CLICKHOUSEASSETS._serialized_start=1974
  _CLICKHOUSEASSETS._serialized_end=2056
# @@protoc_insertion_point(module_scope)
