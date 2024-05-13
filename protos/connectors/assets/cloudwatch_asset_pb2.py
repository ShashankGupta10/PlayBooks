# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/connectors/assets/cloudwatch_asset.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos import base_pb2 as protos_dot_base__pb2
from protos.connectors import connector_pb2 as protos_dot_connectors_dot_connector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/protos/connectors/assets/cloudwatch_asset.proto\x12\x18protos.connectors.assets\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x11protos/base.proto\x1a!protos/connectors/connector.proto\"`\n\x1c\x43loudwatchLogGroupAssetModel\x12,\n\x06region\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x12\n\nlog_groups\x18\x02 \x03(\t\"1\n\x1e\x43loudwatchLogGroupAssetOptions\x12\x0f\n\x07regions\x18\x01 \x03(\t\"\xb3\x03\n\x1a\x43loudwatchMetricAssetModel\x12/\n\tnamespace\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x65\n\x14region_dimension_map\x18\x02 \x03(\x0b\x32G.protos.connectors.assets.CloudwatchMetricAssetModel.RegionDimensionMap\x1a^\n\x0fMetricDimension\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0e\n\x06values\x18\x02 \x03(\t\x12\x0f\n\x07metrics\x18\x03 \x03(\t\x1a\x9c\x01\n\x12RegionDimensionMap\x12,\n\x06region\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12X\n\ndimensions\x18\x02 \x03(\x0b\x32\x44.protos.connectors.assets.CloudwatchMetricAssetModel.MetricDimension\"2\n\x1c\x43loudwatchMetricAssetOptions\x12\x12\n\nnamespaces\x18\x01 \x03(\t\"\xef\x02\n\x14\x43loudwatchAssetModel\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12&\n\x0e\x63onnector_type\x18\x02 \x01(\x0e\x32\x0e.protos.Source\x12;\n\x04type\x18\x03 \x01(\x0e\x32-.protos.connectors.ConnectorMetadataModelType\x12\x14\n\x0clast_updated\x18\x04 \x01(\x10\x12V\n\x14\x63loudwatch_log_group\x18\x05 \x01(\x0b\x32\x36.protos.connectors.assets.CloudwatchLogGroupAssetModelH\x00\x12Q\n\x11\x63loudwatch_metric\x18\x06 \x01(\x0b\x32\x34.protos.connectors.assets.CloudwatchMetricAssetModelH\x00\x42\x07\n\x05\x61sset\"R\n\x10\x43loudwatchAssets\x12>\n\x06\x61ssets\x18\x01 \x03(\x0b\x32..protos.connectors.assets.CloudwatchAssetModelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.connectors.assets.cloudwatch_asset_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLOUDWATCHLOGGROUPASSETMODEL._serialized_start=163
  _CLOUDWATCHLOGGROUPASSETMODEL._serialized_end=259
  _CLOUDWATCHLOGGROUPASSETOPTIONS._serialized_start=261
  _CLOUDWATCHLOGGROUPASSETOPTIONS._serialized_end=310
  _CLOUDWATCHMETRICASSETMODEL._serialized_start=313
  _CLOUDWATCHMETRICASSETMODEL._serialized_end=748
  _CLOUDWATCHMETRICASSETMODEL_METRICDIMENSION._serialized_start=495
  _CLOUDWATCHMETRICASSETMODEL_METRICDIMENSION._serialized_end=589
  _CLOUDWATCHMETRICASSETMODEL_REGIONDIMENSIONMAP._serialized_start=592
  _CLOUDWATCHMETRICASSETMODEL_REGIONDIMENSIONMAP._serialized_end=748
  _CLOUDWATCHMETRICASSETOPTIONS._serialized_start=750
  _CLOUDWATCHMETRICASSETOPTIONS._serialized_end=800
  _CLOUDWATCHASSETMODEL._serialized_start=803
  _CLOUDWATCHASSETMODEL._serialized_end=1170
  _CLOUDWATCHASSETS._serialized_start=1172
  _CLOUDWATCHASSETS._serialized_end=1254
# @@protoc_insertion_point(module_scope)
