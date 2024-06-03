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
import protos.connectors.alert_ops_pb2
import protos.connectors.connector_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CreateConnectorRequest(google.protobuf.message.Message):
    """///////////////////  Connectors API schema  /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_FIELD_NUMBER: builtins.int
    CONNECTOR_KEYS_FIELD_NUMBER: builtins.int
    @property
    def connector(self) -> protos.connectors.connector_pb2.Connector: ...
    @property
    def connector_keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.connector_pb2.ConnectorKey]: ...
    def __init__(
        self,
        *,
        connector: protos.connectors.connector_pb2.Connector | None = ...,
        connector_keys: collections.abc.Iterable[protos.connectors.connector_pb2.ConnectorKey] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector", b"connector"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector", b"connector", "connector_keys", b"connector_keys"]) -> None: ...

global___CreateConnectorRequest = CreateConnectorRequest

@typing_extensions.final
class CreateConnectorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    def __init__(
        self,
        *,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["message", b"message", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["message", b"message", "success", b"success"]) -> None: ...

global___CreateConnectorResponse = CreateConnectorResponse

@typing_extensions.final
class GetConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    @property
    def connector_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    def __init__(
        self,
        *,
        connector_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector_id", b"connector_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_id", b"connector_id"]) -> None: ...

global___GetConnectorRequest = GetConnectorRequest

@typing_extensions.final
class GetConnectorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    CONNECTOR_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    @property
    def connector(self) -> protos.connectors.connector_pb2.Connector: ...
    def __init__(
        self,
        *,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
        connector: protos.connectors.connector_pb2.Connector | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector", b"connector", "message", b"message", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector", b"connector", "message", b"message", "success", b"success"]) -> None: ...

global___GetConnectorResponse = GetConnectorResponse

@typing_extensions.final
class GetConnectorsListRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetConnectorsListRequest = GetConnectorsListRequest

@typing_extensions.final
class GetConnectorsListResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    REQUEST_CONNECTORS_FIELD_NUMBER: builtins.int
    AVAILABLE_CONNECTORS_FIELD_NUMBER: builtins.int
    CONNECTORS_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    @property
    def request_connectors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.connector_pb2.Connector]: ...
    @property
    def available_connectors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.connector_pb2.Connector]: ...
    @property
    def connectors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.connector_pb2.Connector]: ...
    def __init__(
        self,
        *,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
        request_connectors: collections.abc.Iterable[protos.connectors.connector_pb2.Connector] | None = ...,
        available_connectors: collections.abc.Iterable[protos.connectors.connector_pb2.Connector] | None = ...,
        connectors: collections.abc.Iterable[protos.connectors.connector_pb2.Connector] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["message", b"message", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["available_connectors", b"available_connectors", "connectors", b"connectors", "message", b"message", "request_connectors", b"request_connectors", "success", b"success"]) -> None: ...

global___GetConnectorsListResponse = GetConnectorsListResponse

@typing_extensions.final
class UpdateConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    UPDATE_CONNECTOR_OPS_FIELD_NUMBER: builtins.int
    @property
    def connector_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def update_connector_ops(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.connector_pb2.UpdateConnectorOp]: ...
    def __init__(
        self,
        *,
        connector_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        update_connector_ops: collections.abc.Iterable[protos.connectors.connector_pb2.UpdateConnectorOp] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector_id", b"connector_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_id", b"connector_id", "update_connector_ops", b"update_connector_ops"]) -> None: ...

global___UpdateConnectorRequest = UpdateConnectorRequest

@typing_extensions.final
class UpdateConnectorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    def __init__(
        self,
        *,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["message", b"message", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["message", b"message", "success", b"success"]) -> None: ...

global___UpdateConnectorResponse = UpdateConnectorResponse

@typing_extensions.final
class GetConnectorKeysOptionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
    connector_type: protos.base_pb2.Source.ValueType
    def __init__(
        self,
        *,
        connector_type: protos.base_pb2.Source.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_type", b"connector_type"]) -> None: ...

global___GetConnectorKeysOptionsRequest = GetConnectorKeysOptionsRequest

@typing_extensions.final
class GetConnectorKeysOptionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    CONNECTOR_KEY_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    @property
    def connector_key_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.connector_pb2.ConnectorKey]: ...
    def __init__(
        self,
        *,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
        connector_key_options: collections.abc.Iterable[protos.connectors.connector_pb2.ConnectorKey] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["message", b"message", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_key_options", b"connector_key_options", "message", b"message", "success", b"success"]) -> None: ...

global___GetConnectorKeysOptionsResponse = GetConnectorKeysOptionsResponse

@typing_extensions.final
class GetConnectorKeysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
    @property
    def connector_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    connector_type: protos.base_pb2.Source.ValueType
    def __init__(
        self,
        *,
        connector_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        connector_type: protos.base_pb2.Source.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector_id", b"connector_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_id", b"connector_id", "connector_type", b"connector_type"]) -> None: ...

global___GetConnectorKeysRequest = GetConnectorKeysRequest

@typing_extensions.final
class GetConnectorKeysResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    CONNECTOR_FIELD_NUMBER: builtins.int
    CONNECTOR_KEYS_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    @property
    def connector(self) -> protos.connectors.connector_pb2.Connector: ...
    @property
    def connector_keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.connector_pb2.ConnectorKey]: ...
    def __init__(
        self,
        *,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
        connector: protos.connectors.connector_pb2.Connector | None = ...,
        connector_keys: collections.abc.Iterable[protos.connectors.connector_pb2.ConnectorKey] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector", b"connector", "message", b"message", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector", b"connector", "connector_keys", b"connector_keys", "message", b"message", "success", b"success"]) -> None: ...

global___GetConnectorKeysResponse = GetConnectorKeysResponse

@typing_extensions.final
class GetConnectorPlaybookSourceOptionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["meta", b"meta"]) -> None: ...

global___GetConnectorPlaybookSourceOptionsRequest = GetConnectorPlaybookSourceOptionsRequest

@typing_extensions.final
class GetConnectorPlaybookSourceOptionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    ACTIVE_ACCOUNT_CONNECTORS_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def active_account_connectors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.connector_pb2.AccountActiveConnectorModelTypes]: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        active_account_connectors: collections.abc.Iterable[protos.connectors.connector_pb2.AccountActiveConnectorModelTypes] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta", b"meta", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["active_account_connectors", b"active_account_connectors", "meta", b"meta", "success", b"success"]) -> None: ...

global___GetConnectorPlaybookSourceOptionsResponse = GetConnectorPlaybookSourceOptionsResponse

@typing_extensions.final
class GetSlackAlertTriggerOptionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ConnectorTypeRequest(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
        FILTER_CHANNELS_FIELD_NUMBER: builtins.int
        FILTER_ALERT_TYPES_FIELD_NUMBER: builtins.int
        FILTER_ALERT_TAGS_FIELD_NUMBER: builtins.int
        connector_type: protos.base_pb2.Source.ValueType
        @property
        def filter_channels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
        @property
        def filter_alert_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
        @property
        def filter_alert_tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
        def __init__(
            self,
            *,
            connector_type: protos.base_pb2.Source.ValueType = ...,
            filter_channels: collections.abc.Iterable[builtins.str] | None = ...,
            filter_alert_types: collections.abc.Iterable[builtins.str] | None = ...,
            filter_alert_tags: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["connector_type", b"connector_type", "filter_alert_tags", b"filter_alert_tags", "filter_alert_types", b"filter_alert_types", "filter_channels", b"filter_channels"]) -> None: ...

    META_FIELD_NUMBER: builtins.int
    CONNECTOR_TYPE_REQUESTS_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    @property
    def connector_type_requests(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetSlackAlertTriggerOptionsRequest.ConnectorTypeRequest]: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        connector_type_requests: collections.abc.Iterable[global___GetSlackAlertTriggerOptionsRequest.ConnectorTypeRequest] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector_type_requests", b"connector_type_requests", "meta", b"meta"]) -> None: ...

global___GetSlackAlertTriggerOptionsRequest = GetSlackAlertTriggerOptionsRequest

@typing_extensions.final
class GetSlackAlertTriggerOptionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    ALERT_OPS_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    @property
    def alert_ops_options(self) -> protos.connectors.alert_ops_pb2.AlertOpsOptions: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        alert_ops_options: protos.connectors.alert_ops_pb2.AlertOpsOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["alert_ops_options", b"alert_ops_options", "meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_ops_options", b"alert_ops_options", "meta", b"meta"]) -> None: ...

global___GetSlackAlertTriggerOptionsResponse = GetSlackAlertTriggerOptionsResponse

@typing_extensions.final
class GetSlackAlertsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    USE_DB_SOURCE_TAGS_FIELD_NUMBER: builtins.int
    WORKSPACE_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    ALERT_TYPE_FIELD_NUMBER: builtins.int
    PATTERN_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    @property
    def use_db_source_tags(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def workspace_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def channel_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def alert_type(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def pattern(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        use_db_source_tags: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        workspace_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        channel_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        alert_type: google.protobuf.wrappers_pb2.StringValue | None = ...,
        pattern: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["alert_type", b"alert_type", "channel_id", b"channel_id", "meta", b"meta", "pattern", b"pattern", "use_db_source_tags", b"use_db_source_tags", "workspace_id", b"workspace_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_type", b"alert_type", "channel_id", b"channel_id", "meta", b"meta", "pattern", b"pattern", "use_db_source_tags", b"use_db_source_tags", "workspace_id", b"workspace_id"]) -> None: ...

global___GetSlackAlertsRequest = GetSlackAlertsRequest

@typing_extensions.final
class GetSlackAlertsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    SLACK_ALERTS_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    @property
    def slack_alerts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.connectors.alert_ops_pb2.SlackAlert]: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        slack_alerts: collections.abc.Iterable[protos.connectors.alert_ops_pb2.SlackAlert] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["meta", b"meta", "slack_alerts", b"slack_alerts"]) -> None: ...

global___GetSlackAlertsResponse = GetSlackAlertsResponse

@typing_extensions.final
class GetSlackAppManifestRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_NAME_FIELD_NUMBER: builtins.int
    @property
    def host_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        host_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["host_name", b"host_name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_name", b"host_name"]) -> None: ...

global___GetSlackAppManifestRequest = GetSlackAppManifestRequest

@typing_extensions.final
class GetSlackAppManifestResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    APP_MANIFEST_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    @property
    def app_manifest(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
        app_manifest: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["app_manifest", b"app_manifest", "message", b"message", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_manifest", b"app_manifest", "message", b"message", "success", b"success"]) -> None: ...

global___GetSlackAppManifestResponse = GetSlackAppManifestResponse

@typing_extensions.final
class GetConnectedPlaybooksRequest(google.protobuf.message.Message):
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

global___GetConnectedPlaybooksRequest = GetConnectedPlaybooksRequest

@typing_extensions.final
class GetConnectedPlaybooksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Playbook(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PLAYBOOK_ID_FIELD_NUMBER: builtins.int
        PLAYBOOK_NAME_FIELD_NUMBER: builtins.int
        @property
        def playbook_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
        @property
        def playbook_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            playbook_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
            playbook_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["playbook_id", b"playbook_id", "playbook_name", b"playbook_name"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["playbook_id", b"playbook_id", "playbook_name", b"playbook_name"]) -> None: ...

    META_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    CONNECTED_PLAYBOOKS_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> protos.base_pb2.Meta: ...
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def message(self) -> protos.base_pb2.Message: ...
    @property
    def connected_playbooks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetConnectedPlaybooksResponse.Playbook]: ...
    def __init__(
        self,
        *,
        meta: protos.base_pb2.Meta | None = ...,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        message: protos.base_pb2.Message | None = ...,
        connected_playbooks: collections.abc.Iterable[global___GetConnectedPlaybooksResponse.Playbook] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["message", b"message", "meta", b"meta", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connected_playbooks", b"connected_playbooks", "message", b"message", "meta", b"meta", "success", b"success"]) -> None: ...

global___GetConnectedPlaybooksResponse = GetConnectedPlaybooksResponse
