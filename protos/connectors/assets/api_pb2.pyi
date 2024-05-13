"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import protos.base_pb2
import protos.connectors.assets.asset_pb2
import protos.connectors.connector_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class GetConnectorsAssetsModelsOptionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
    MODEL_TYPE_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    connector_type: protos.base_pb2.Source.ValueType
    model_type: protos.connectors.connector_pb2.ConnectorMetadataModelType.ValueType
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        connector_type: protos.base_pb2.Source.ValueType = ...,
        model_type: protos.connectors.connector_pb2.ConnectorMetadataModelType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_type", b"connector_type", "meta", b"meta", "model_type", b"model_type"]) -> None: ...

global___GetConnectorsAssetsModelsOptionsRequest = GetConnectorsAssetsModelsOptionsRequest

@typing_extensions.final
class GetConnectorsAssetsModelsOptionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    ASSET_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    @property
    def asset_model_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.assets.asset_pb2.AccountConnectorAssetsModelOptions]: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
        asset_model_options: collections.abc.Iterable[protos.connectors.assets.asset_pb2.AccountConnectorAssetsModelOptions] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["message", b"message", "meta", b"meta", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_model_options", b"asset_model_options", "message", b"message", "meta", b"meta", "success", b"success"]) -> None: ...

global___GetConnectorsAssetsModelsOptionsResponse = GetConnectorsAssetsModelsOptionsResponse

@typing_extensions.final
class GetConnectorsAssetsModelsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    FILTERS_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    connector_type: protos.base_pb2.Source.ValueType
    type: protos.connectors.connector_pb2.ConnectorMetadataModelType.ValueType
    @property
    def filters(self) -> protos.connectors.assets.asset_pb2.AccountConnectorAssetsModelFilters: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        connector_type: protos.base_pb2.Source.ValueType = ...,
        type: protos.connectors.connector_pb2.ConnectorMetadataModelType.ValueType = ...,
        filters: protos.connectors.assets.asset_pb2.AccountConnectorAssetsModelFilters | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filters", b"filters", "meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_type", b"connector_type", "filters", b"filters", "meta", b"meta", "type", b"type"]) -> None: ...

global___GetConnectorsAssetsModelsRequest = GetConnectorsAssetsModelsRequest

@typing_extensions.final
class GetConnectorsAssetsModelsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    ASSETS_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    @property
    def assets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.assets.asset_pb2.AccountConnectorAssets]: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
        assets: collections.abc.Iterable[protos.connectors.assets.asset_pb2.AccountConnectorAssets] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["message", b"message", "meta", b"meta", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assets", b"assets", "message", b"message", "meta", b"meta", "success", b"success"]) -> None: ...

global___GetConnectorsAssetsModelsResponse = GetConnectorsAssetsModelsResponse

@typing_extensions.final
class GetConnectorsAssetsModelsRefreshRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    @property
    def connector_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        connector_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector_id", b"connector_id", "meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_id", b"connector_id", "meta", b"meta"]) -> None: ...

global___GetConnectorsAssetsModelsRefreshRequest = GetConnectorsAssetsModelsRefreshRequest

@typing_extensions.final
class GetConnectorsAssetsModelsRefreshResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["message", b"message", "meta", b"meta", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["message", b"message", "meta", b"meta", "success", b"success"]) -> None: ...

global___GetConnectorsAssetsModelsRefreshResponse = GetConnectorsAssetsModelsRefreshResponse
