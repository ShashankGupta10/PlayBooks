# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from protos import base_pb2 as protos_dot_base__pb2
from protos import query_base_pb2 as protos_dot_query__base__pb2
from protos.playbooks import deprecated_playbook_pb2 as protos_dot_playbooks_dot_deprecated__playbook__pb2
from protos.playbooks import playbook_pb2 as protos_dot_playbooks_dot_playbook__pb2
from protos.playbooks import workflow_pb2 as protos_dot_playbooks_dot_workflow__pb2
from protos.playbooks.intelligence_layer import interpreter_pb2 as protos_dot_playbooks_dot_intelligence__layer_dot_interpreter__pb2
from protos.playbooks import playbook_commons_pb2 as protos_dot_playbooks_dot_playbook__commons__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aprotos/playbooks/api.proto\x12\x10protos.playbooks\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x11protos/base.proto\x1a\x17protos/query_base.proto\x1a*protos/playbooks/deprecated_playbook.proto\x1a\x1fprotos/playbooks/playbook.proto\x1a\x1fprotos/playbooks/workflow.proto\x1a\x35protos/playbooks/intelligence_layer/interpreter.proto\x1a\'protos/playbooks/playbook_commons.proto\"\x8a\x01\n\x16RunPlaybookTaskRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12T\n\x18playbook_task_definition\x18\x02 \x01(\x0b\x32\x32.protos.playbooks.DeprecatedPlaybookTaskDefinition\"\xdc\x01\n\x17RunPlaybookTaskResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12V\n\x15task_execution_result\x18\x04 \x01(\x0b\x32\x37.protos.playbooks.DeprecatedPlaybookTaskExecutionResult\"\xd4\x01\n\x19RunPlaybookTaskResponseV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12L\n\x12task_execution_log\x18\x04 \x01(\x0b\x32\x30.protos.playbooks.DeprecatedPlaybookExecutionLog\"\xa3\x01\n\x18RunPlaybookTaskRequestV3\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x34\n\x13global_variable_set\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x35\n\rplaybook_task\x18\x03 \x01(\x0b\x32\x1e.protos.playbooks.PlaybookTask\"\xd7\x01\n\x19RunPlaybookTaskResponseV3\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12O\n\x1bplaybook_task_execution_log\x18\x04 \x01(\x0b\x32*.protos.playbooks.PlaybookTaskExecutionLog\"\x7f\n\x16RunPlaybookStepRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12I\n\rplaybook_step\x18\x02 \x01(\x0b\x32\x32.protos.playbooks.DeprecatedPlaybookStepDefinition\"\xbc\x02\n\x17RunPlaybookStepResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12W\n\x16task_execution_results\x18\x06 \x03(\x0b\x32\x37.protos.playbooks.DeprecatedPlaybookTaskExecutionResult\"\xd8\x01\n\x19RunPlaybookStepResponseV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12P\n\x12step_execution_log\x18\x04 \x01(\x0b\x32\x34.protos.playbooks.DeprecatedPlaybookStepExecutionLog\"m\n\x18RunPlaybookStepRequestV3\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x35\n\rplaybook_step\x18\x02 \x01(\x0b\x32\x1e.protos.playbooks.PlaybookStep\"\xce\x01\n\x19RunPlaybookStepResponseV3\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12\x46\n\x12step_execution_log\x18\x04 \x01(\x0b\x32*.protos.playbooks.PlaybookStepExecutionLog\"h\n\x12RunPlaybookRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x36\n\x08playbook\x18\x02 \x01(\x0b\x32$.protos.playbooks.DeprecatedPlaybook\"\xcb\x01\n\x13RunPlaybookResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12I\n\x12playbook_execution\x18\x04 \x01(\x0b\x32-.protos.playbooks.DeprecatedPlaybookExecution\"`\n\x14RunPlaybookRequestV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12,\n\x08playbook\x18\x02 \x01(\x0b\x32\x1a.protos.playbooks.Playbook\"\xc3\x01\n\x15RunPlaybookResponseV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12?\n\x12playbook_execution\x18\x04 \x01(\x0b\x32#.protos.playbooks.PlaybookExecution\"G\n\x13GetPlaybooksRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x14\n\x0cplaybook_ids\x18\x02 \x03(\x04\"k\n\x14GetPlaybooksResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x37\n\tplaybooks\x18\x02 \x03(\x0b\x32$.protos.playbooks.DeprecatedPlaybook\"I\n\x15GetPlaybooksRequestV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x14\n\x0cplaybook_ids\x18\x02 \x03(\x04\"c\n\x16GetPlaybooksResponseV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12-\n\tplaybooks\x18\x02 \x03(\x0b\x32\x1a.protos.playbooks.Playbook\"a\n\x16SearchPlaybooksRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\rquery_request\x18\x02 \x01(\x0b\x32\x14.protos.QueryRequest\"d\n\x17SearchPlaybooksResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12-\n\tplaybooks\x18\x02 \x03(\x0b\x32\x1a.protos.playbooks.Playbook\"]\n\x15\x43reatePlaybookRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x08playbook\x18\x02 \x01(\x0b\x32$.protos.playbooks.DeprecatedPlaybook\"\x9f\x01\n\x16\x43reatePlaybookResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12\x36\n\x08playbook\x18\x03 \x01(\x0b\x32$.protos.playbooks.DeprecatedPlaybook\"U\n\x17\x43reatePlaybookRequestV2\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x08playbook\x18\x02 \x01(\x0b\x32\x1a.protos.playbooks.Playbook\"\x97\x01\n\x18\x43reatePlaybookResponseV2\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12,\n\x08playbook\x18\x03 \x01(\x0b\x32\x1a.protos.playbooks.Playbook\"\x95\x01\n\x15UpdatePlaybookRequest\x12\x31\n\x0bplaybook_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12I\n\x13update_playbook_ops\x18\x02 \x03(\x0b\x32,.protos.playbooks.DeprecatedUpdatePlaybookOp\"g\n\x16UpdatePlaybookResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"\x8d\x01\n\x17UpdatePlaybookRequestV2\x12\x31\n\x0bplaybook_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12?\n\x13update_playbook_ops\x18\x02 \x03(\x0b\x32\".protos.playbooks.UpdatePlaybookOp\"i\n\x18UpdatePlaybookResponseV2\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"g\n\x16\x45xecutePlaybookRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x31\n\x0bplaybook_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"\xbb\x01\n\x17\x45xecutePlaybookResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12\x35\n\x0fplaybook_run_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"p\n\x1b\x45xecutionPlaybookGetRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x35\n\x0fplaybook_run_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xd4\x01\n\x1c\x45xecutionPlaybookGetResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12I\n\x12playbook_execution\x18\x04 \x01(\x0b\x32-.protos.playbooks.DeprecatedPlaybookExecution\"r\n\x1d\x45xecutionPlaybookGetRequestV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x35\n\x0fplaybook_run_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xcc\x01\n\x1e\x45xecutionPlaybookGetResponseV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12?\n\x12playbook_execution\x18\x04 \x01(\x0b\x32#.protos.playbooks.PlaybookExecution\"i\n\x1e\x45xecutionPlaybookSearchRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\rquery_request\x18\x02 \x01(\x0b\x32\x14.protos.QueryRequest\"\xac\x01\n\x1f\x45xecutionPlaybookSearchResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12@\n\x13playbook_executions\x18\x03 \x03(\x0b\x32#.protos.playbooks.PlaybookExecution\"\xd8\x01\n\x1f\x45xecutionPlaybookAPIGetResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12J\n\x13playbook_executions\x18\x04 \x03(\x0b\x32-.protos.playbooks.DeprecatedPlaybookExecution\"\xd0\x01\n!ExecutionPlaybookAPIGetResponseV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12@\n\x13playbook_executions\x18\x04 \x03(\x0b\x32#.protos.playbooks.PlaybookExecution\"R\n\x1e\x45xecutionsPlaybooksListRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x14\n\x0cplaybook_ids\x18\x02 \x03(\t\"\xce\x01\n\x1f\x45xecutionsPlaybooksListResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12@\n\x13playbook_executions\x18\x04 \x03(\x0b\x32#.protos.playbooks.PlaybookExecution\"\x94\x01\n\x1cPlaybookTemplatesGetResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12%\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Struct\"o\n\x1ePlaybookExecutionCreateRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x31\n\x0bplaybook_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"\x80\x02\n\x1fPlaybookExecutionCreateResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12\x35\n\x0fplaybook_run_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15\x65xecution_session_url\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xa6\x01\n#PlaybookExecutionStepExecuteRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x35\n\x0fplaybook_run_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x04step\x18\x03 \x01(\x0b\x32\x1e.protos.playbooks.PlaybookStep\"\x90\x02\n$PlaybookExecutionStepExecuteResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12\x35\n\x0fplaybook_run_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x46\n\x12step_execution_log\x18\x05 \x01(\x0b\x32*.protos.playbooks.PlaybookStepExecutionLog\"G\n\x13GetWorkflowsRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x14\n\x0cworkflow_ids\x18\x02 \x03(\x04\"a\n\x14GetWorkflowsResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12-\n\tworkflows\x18\x02 \x03(\x0b\x32\x1a.protos.playbooks.Workflow\"a\n\x16SearchWorkflowsRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\rquery_request\x18\x02 \x01(\x0b\x32\x14.protos.QueryRequest\"d\n\x17SearchWorkflowsResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12-\n\tworkflows\x18\x02 \x03(\x0b\x32\x1a.protos.playbooks.Workflow\"S\n\x15\x43reateWorkflowRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x08workflow\x18\x02 \x01(\x0b\x32\x1a.protos.playbooks.Workflow\"\x95\x01\n\x16\x43reateWorkflowResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12,\n\x08workflow\x18\x03 \x01(\x0b\x32\x1a.protos.playbooks.Workflow\"\x8b\x01\n\x15UpdateWorkflowRequest\x12\x31\n\x0bworkflow_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12?\n\x13update_workflow_ops\x18\x02 \x03(\x0b\x32\".protos.playbooks.UpdateWorkflowOp\"g\n\x16UpdateWorkflowResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"\xe5\x01\n\x16\x45xecuteWorkflowRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x31\n\x0bworkflow_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x33\n\rworkflow_name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12G\n\x16workflow_configuration\x18\x04 \x01(\x0b\x32\'.protos.playbooks.WorkflowConfiguration\"\xbb\x01\n\x17\x45xecuteWorkflowResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12\x35\n\x0fworkflow_run_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"v\n\x1b\x45xecutionWorkflowGetRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12;\n\x15workflow_execution_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"\xca\x01\n\x1c\x45xecutionWorkflowGetResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12?\n\x12workflow_execution\x18\x04 \x01(\x0b\x32#.protos.playbooks.WorkflowExecution\"i\n\x1e\x45xecutionWorkflowSearchRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\rquery_request\x18\x02 \x01(\x0b\x32\x14.protos.QueryRequest\"\xac\x01\n\x1f\x45xecutionWorkflowSearchResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12@\n\x13workflow_executions\x18\x03 \x03(\x0b\x32#.protos.playbooks.WorkflowExecution\"R\n\x1e\x45xecutionsWorkflowsListRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x14\n\x0cworkflow_ids\x18\x02 \x03(\t\"\xce\x01\n\x1f\x45xecutionsWorkflowsListResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12@\n\x13workflow_executions\x18\x04 \x03(\x0b\x32#.protos.playbooks.WorkflowExecution\"u\n ExecutionsWorkflowsGetAllRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x35\n\x0fworkflow_run_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xd0\x01\n!ExecutionsWorkflowsGetAllResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12@\n\x13workflow_executions\x18\x04 \x03(\x0b\x32#.protos.playbooks.WorkflowExecution\"<\n\x1ePlaybooksBuilderOptionsRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\"\xaf\x03\n\x1fPlaybooksBuilderOptionsResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12\x62\n\x11interpreter_types\x18\x04 \x03(\x0b\x32G.protos.playbooks.PlaybooksBuilderOptionsResponse.InterpreterTypeOption\x12?\n\x0esource_options\x18\x05 \x03(\x0b\x32\'.protos.playbooks.PlaybookSourceOptions\x1a|\n\x15InterpreterTypeOption\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.protos.playbooks.InterpreterType\x12\x32\n\x0c\x64isplay_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RUNPLAYBOOKTASKREQUEST._serialized_start=361
  _RUNPLAYBOOKTASKREQUEST._serialized_end=499
  _RUNPLAYBOOKTASKRESPONSE._serialized_start=502
  _RUNPLAYBOOKTASKRESPONSE._serialized_end=722
  _RUNPLAYBOOKTASKRESPONSEV2._serialized_start=725
  _RUNPLAYBOOKTASKRESPONSEV2._serialized_end=937
  _RUNPLAYBOOKTASKREQUESTV3._serialized_start=940
  _RUNPLAYBOOKTASKREQUESTV3._serialized_end=1103
  _RUNPLAYBOOKTASKRESPONSEV3._serialized_start=1106
  _RUNPLAYBOOKTASKRESPONSEV3._serialized_end=1321
  _RUNPLAYBOOKSTEPREQUEST._serialized_start=1323
  _RUNPLAYBOOKSTEPREQUEST._serialized_end=1450
  _RUNPLAYBOOKSTEPRESPONSE._serialized_start=1453
  _RUNPLAYBOOKSTEPRESPONSE._serialized_end=1769
  _RUNPLAYBOOKSTEPRESPONSEV2._serialized_start=1772
  _RUNPLAYBOOKSTEPRESPONSEV2._serialized_end=1988
  _RUNPLAYBOOKSTEPREQUESTV3._serialized_start=1990
  _RUNPLAYBOOKSTEPREQUESTV3._serialized_end=2099
  _RUNPLAYBOOKSTEPRESPONSEV3._serialized_start=2102
  _RUNPLAYBOOKSTEPRESPONSEV3._serialized_end=2308
  _RUNPLAYBOOKREQUEST._serialized_start=2310
  _RUNPLAYBOOKREQUEST._serialized_end=2414
  _RUNPLAYBOOKRESPONSE._serialized_start=2417
  _RUNPLAYBOOKRESPONSE._serialized_end=2620
  _RUNPLAYBOOKREQUESTV2._serialized_start=2622
  _RUNPLAYBOOKREQUESTV2._serialized_end=2718
  _RUNPLAYBOOKRESPONSEV2._serialized_start=2721
  _RUNPLAYBOOKRESPONSEV2._serialized_end=2916
  _GETPLAYBOOKSREQUEST._serialized_start=2918
  _GETPLAYBOOKSREQUEST._serialized_end=2989
  _GETPLAYBOOKSRESPONSE._serialized_start=2991
  _GETPLAYBOOKSRESPONSE._serialized_end=3098
  _GETPLAYBOOKSREQUESTV2._serialized_start=3100
  _GETPLAYBOOKSREQUESTV2._serialized_end=3173
  _GETPLAYBOOKSRESPONSEV2._serialized_start=3175
  _GETPLAYBOOKSRESPONSEV2._serialized_end=3274
  _SEARCHPLAYBOOKSREQUEST._serialized_start=3276
  _SEARCHPLAYBOOKSREQUEST._serialized_end=3373
  _SEARCHPLAYBOOKSRESPONSE._serialized_start=3375
  _SEARCHPLAYBOOKSRESPONSE._serialized_end=3475
  _CREATEPLAYBOOKREQUEST._serialized_start=3477
  _CREATEPLAYBOOKREQUEST._serialized_end=3570
  _CREATEPLAYBOOKRESPONSE._serialized_start=3573
  _CREATEPLAYBOOKRESPONSE._serialized_end=3732
  _CREATEPLAYBOOKREQUESTV2._serialized_start=3734
  _CREATEPLAYBOOKREQUESTV2._serialized_end=3819
  _CREATEPLAYBOOKRESPONSEV2._serialized_start=3822
  _CREATEPLAYBOOKRESPONSEV2._serialized_end=3973
  _UPDATEPLAYBOOKREQUEST._serialized_start=3976
  _UPDATEPLAYBOOKREQUEST._serialized_end=4125
  _UPDATEPLAYBOOKRESPONSE._serialized_start=4127
  _UPDATEPLAYBOOKRESPONSE._serialized_end=4230
  _UPDATEPLAYBOOKREQUESTV2._serialized_start=4233
  _UPDATEPLAYBOOKREQUESTV2._serialized_end=4374
  _UPDATEPLAYBOOKRESPONSEV2._serialized_start=4376
  _UPDATEPLAYBOOKRESPONSEV2._serialized_end=4481
  _EXECUTEPLAYBOOKREQUEST._serialized_start=4483
  _EXECUTEPLAYBOOKREQUEST._serialized_end=4586
  _EXECUTEPLAYBOOKRESPONSE._serialized_start=4589
  _EXECUTEPLAYBOOKRESPONSE._serialized_end=4776
  _EXECUTIONPLAYBOOKGETREQUEST._serialized_start=4778
  _EXECUTIONPLAYBOOKGETREQUEST._serialized_end=4890
  _EXECUTIONPLAYBOOKGETRESPONSE._serialized_start=4893
  _EXECUTIONPLAYBOOKGETRESPONSE._serialized_end=5105
  _EXECUTIONPLAYBOOKGETREQUESTV2._serialized_start=5107
  _EXECUTIONPLAYBOOKGETREQUESTV2._serialized_end=5221
  _EXECUTIONPLAYBOOKGETRESPONSEV2._serialized_start=5224
  _EXECUTIONPLAYBOOKGETRESPONSEV2._serialized_end=5428
  _EXECUTIONPLAYBOOKSEARCHREQUEST._serialized_start=5430
  _EXECUTIONPLAYBOOKSEARCHREQUEST._serialized_end=5535
  _EXECUTIONPLAYBOOKSEARCHRESPONSE._serialized_start=5538
  _EXECUTIONPLAYBOOKSEARCHRESPONSE._serialized_end=5710
  _EXECUTIONPLAYBOOKAPIGETRESPONSE._serialized_start=5713
  _EXECUTIONPLAYBOOKAPIGETRESPONSE._serialized_end=5929
  _EXECUTIONPLAYBOOKAPIGETRESPONSEV2._serialized_start=5932
  _EXECUTIONPLAYBOOKAPIGETRESPONSEV2._serialized_end=6140
  _EXECUTIONSPLAYBOOKSLISTREQUEST._serialized_start=6142
  _EXECUTIONSPLAYBOOKSLISTREQUEST._serialized_end=6224
  _EXECUTIONSPLAYBOOKSLISTRESPONSE._serialized_start=6227
  _EXECUTIONSPLAYBOOKSLISTRESPONSE._serialized_end=6433
  _PLAYBOOKTEMPLATESGETRESPONSE._serialized_start=6436
  _PLAYBOOKTEMPLATESGETRESPONSE._serialized_end=6584
  _PLAYBOOKEXECUTIONCREATEREQUEST._serialized_start=6586
  _PLAYBOOKEXECUTIONCREATEREQUEST._serialized_end=6697
  _PLAYBOOKEXECUTIONCREATERESPONSE._serialized_start=6700
  _PLAYBOOKEXECUTIONCREATERESPONSE._serialized_end=6956
  _PLAYBOOKEXECUTIONSTEPEXECUTEREQUEST._serialized_start=6959
  _PLAYBOOKEXECUTIONSTEPEXECUTEREQUEST._serialized_end=7125
  _PLAYBOOKEXECUTIONSTEPEXECUTERESPONSE._serialized_start=7128
  _PLAYBOOKEXECUTIONSTEPEXECUTERESPONSE._serialized_end=7400
  _GETWORKFLOWSREQUEST._serialized_start=7402
  _GETWORKFLOWSREQUEST._serialized_end=7473
  _GETWORKFLOWSRESPONSE._serialized_start=7475
  _GETWORKFLOWSRESPONSE._serialized_end=7572
  _SEARCHWORKFLOWSREQUEST._serialized_start=7574
  _SEARCHWORKFLOWSREQUEST._serialized_end=7671
  _SEARCHWORKFLOWSRESPONSE._serialized_start=7673
  _SEARCHWORKFLOWSRESPONSE._serialized_end=7773
  _CREATEWORKFLOWREQUEST._serialized_start=7775
  _CREATEWORKFLOWREQUEST._serialized_end=7858
  _CREATEWORKFLOWRESPONSE._serialized_start=7861
  _CREATEWORKFLOWRESPONSE._serialized_end=8010
  _UPDATEWORKFLOWREQUEST._serialized_start=8013
  _UPDATEWORKFLOWREQUEST._serialized_end=8152
  _UPDATEWORKFLOWRESPONSE._serialized_start=8154
  _UPDATEWORKFLOWRESPONSE._serialized_end=8257
  _EXECUTEWORKFLOWREQUEST._serialized_start=8260
  _EXECUTEWORKFLOWREQUEST._serialized_end=8489
  _EXECUTEWORKFLOWRESPONSE._serialized_start=8492
  _EXECUTEWORKFLOWRESPONSE._serialized_end=8679
  _EXECUTIONWORKFLOWGETREQUEST._serialized_start=8681
  _EXECUTIONWORKFLOWGETREQUEST._serialized_end=8799
  _EXECUTIONWORKFLOWGETRESPONSE._serialized_start=8802
  _EXECUTIONWORKFLOWGETRESPONSE._serialized_end=9004
  _EXECUTIONWORKFLOWSEARCHREQUEST._serialized_start=9006
  _EXECUTIONWORKFLOWSEARCHREQUEST._serialized_end=9111
  _EXECUTIONWORKFLOWSEARCHRESPONSE._serialized_start=9114
  _EXECUTIONWORKFLOWSEARCHRESPONSE._serialized_end=9286
  _EXECUTIONSWORKFLOWSLISTREQUEST._serialized_start=9288
  _EXECUTIONSWORKFLOWSLISTREQUEST._serialized_end=9370
  _EXECUTIONSWORKFLOWSLISTRESPONSE._serialized_start=9373
  _EXECUTIONSWORKFLOWSLISTRESPONSE._serialized_end=9579
  _EXECUTIONSWORKFLOWSGETALLREQUEST._serialized_start=9581
  _EXECUTIONSWORKFLOWSGETALLREQUEST._serialized_end=9698
  _EXECUTIONSWORKFLOWSGETALLRESPONSE._serialized_start=9701
  _EXECUTIONSWORKFLOWSGETALLRESPONSE._serialized_end=9909
  _PLAYBOOKSBUILDEROPTIONSREQUEST._serialized_start=9911
  _PLAYBOOKSBUILDEROPTIONSREQUEST._serialized_end=9971
  _PLAYBOOKSBUILDEROPTIONSRESPONSE._serialized_start=9974
  _PLAYBOOKSBUILDEROPTIONSRESPONSE._serialized_end=10405
  _PLAYBOOKSBUILDEROPTIONSRESPONSE_INTERPRETERTYPEOPTION._serialized_start=10281
  _PLAYBOOKSBUILDEROPTIONSRESPONSE_INTERPRETERTYPEOPTION._serialized_end=10405
# @@protoc_insertion_point(module_scope)
