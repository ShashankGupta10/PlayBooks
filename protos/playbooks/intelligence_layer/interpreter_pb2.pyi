"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _InterpreterType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _InterpreterTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_InterpreterType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_I: _InterpreterType.ValueType  # 0
    BASIC_I: _InterpreterType.ValueType  # 1
    STATISTICAL_I: _InterpreterType.ValueType  # 2
    LLM_CHAT_GPT_VISION_I: _InterpreterType.ValueType  # 3

class InterpreterType(_InterpreterType, metaclass=_InterpreterTypeEnumTypeWrapper): ...

UNKNOWN_I: InterpreterType.ValueType  # 0
BASIC_I: InterpreterType.ValueType  # 1
STATISTICAL_I: InterpreterType.ValueType  # 2
LLM_CHAT_GPT_VISION_I: InterpreterType.ValueType  # 3
global___InterpreterType = InterpreterType

@typing_extensions.final
class Interpretation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Interpretation._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: Interpretation._Type.ValueType  # 0
        IMAGE: Interpretation._Type.ValueType  # 1
        TEXT: Interpretation._Type.ValueType  # 2
        CSV_FILE: Interpretation._Type.ValueType  # 3
        JSON: Interpretation._Type.ValueType  # 4

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    UNKNOWN: Interpretation.Type.ValueType  # 0
    IMAGE: Interpretation.Type.ValueType  # 1
    TEXT: Interpretation.Type.ValueType  # 2
    CSV_FILE: Interpretation.Type.ValueType  # 3
    JSON: Interpretation.Type.ValueType  # 4

    class _ModelType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ModelTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Interpretation._ModelType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN_M: Interpretation._ModelType.ValueType  # 0
        PLAYBOOK_TASK: Interpretation._ModelType.ValueType  # 1
        PLAYBOOK_STEP: Interpretation._ModelType.ValueType  # 2
        PLAYBOOK_STEP_RELATION: Interpretation._ModelType.ValueType  # 3
        WORKFLOW_EXECUTION: Interpretation._ModelType.ValueType  # 4

    class ModelType(_ModelType, metaclass=_ModelTypeEnumTypeWrapper): ...
    UNKNOWN_M: Interpretation.ModelType.ValueType  # 0
    PLAYBOOK_TASK: Interpretation.ModelType.ValueType  # 1
    PLAYBOOK_STEP: Interpretation.ModelType.ValueType  # 2
    PLAYBOOK_STEP_RELATION: Interpretation.ModelType.ValueType  # 3
    WORKFLOW_EXECUTION: Interpretation.ModelType.ValueType  # 4

    TYPE_FIELD_NUMBER: builtins.int
    INTERPRETER_TYPE_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SUMMARY_FIELD_NUMBER: builtins.int
    IMAGE_URL_FIELD_NUMBER: builtins.int
    FILE_PATH_FIELD_NUMBER: builtins.int
    OBJECT_URL_FIELD_NUMBER: builtins.int
    MODEL_TYPE_FIELD_NUMBER: builtins.int
    type: global___Interpretation.Type.ValueType
    interpreter_type: global___InterpreterType.ValueType
    @property
    def title(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def summary(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def image_url(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def file_path(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def object_url(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    model_type: global___Interpretation.ModelType.ValueType
    def __init__(
        self,
        *,
        type: global___Interpretation.Type.ValueType = ...,
        interpreter_type: global___InterpreterType.ValueType = ...,
        title: google.protobuf.wrappers_pb2.StringValue | None = ...,
        description: google.protobuf.wrappers_pb2.StringValue | None = ...,
        summary: google.protobuf.wrappers_pb2.StringValue | None = ...,
        image_url: google.protobuf.wrappers_pb2.StringValue | None = ...,
        file_path: google.protobuf.wrappers_pb2.StringValue | None = ...,
        object_url: google.protobuf.wrappers_pb2.StringValue | None = ...,
        model_type: global___Interpretation.ModelType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["description", b"description", "file_path", b"file_path", "image_url", b"image_url", "object_url", b"object_url", "summary", b"summary", "title", b"title"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "file_path", b"file_path", "image_url", b"image_url", "interpreter_type", b"interpreter_type", "model_type", b"model_type", "object_url", b"object_url", "summary", b"summary", "title", b"title", "type", b"type"]) -> None: ...

global___Interpretation = Interpretation
