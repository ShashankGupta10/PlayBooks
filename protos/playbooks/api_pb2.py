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
from protos.playbooks import playbook_pb2 as protos_dot_playbooks_dot_playbook__pb2
from protos.playbooks import workflow_pb2 as protos_dot_playbooks_dot_workflow__pb2
from protos.playbooks.intelligence_layer import interpreter_pb2 as protos_dot_playbooks_dot_intelligence__layer_dot_interpreter__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aprotos/playbooks/api.proto\x12\x10protos.playbooks\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x11protos/base.proto\x1a\x1fprotos/playbooks/playbook.proto\x1a\x1fprotos/playbooks/workflow.proto\x1a\x35protos/playbooks/intelligence_layer/interpreter.proto\"\x80\x01\n\x16RunPlaybookTaskRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12J\n\x18playbook_task_definition\x18\x02 \x01(\x0b\x32(.protos.playbooks.PlaybookTaskDefinition\"\xd2\x01\n\x17RunPlaybookTaskResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12L\n\x15task_execution_result\x18\x04 \x01(\x0b\x32-.protos.playbooks.PlaybookTaskExecutionResult\"\xca\x01\n\x19RunPlaybookTaskResponseV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12\x42\n\x12task_execution_log\x18\x04 \x01(\x0b\x32&.protos.playbooks.PlaybookExecutionLog\"u\n\x16RunPlaybookStepRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12?\n\rplaybook_step\x18\x02 \x01(\x0b\x32(.protos.playbooks.PlaybookStepDefinition\"\xb2\x02\n\x17RunPlaybookStepResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12M\n\x16task_execution_results\x18\x06 \x03(\x0b\x32-.protos.playbooks.PlaybookTaskExecutionResult\"\xce\x01\n\x19RunPlaybookStepResponseV2\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12\x46\n\x12step_execution_log\x18\x04 \x01(\x0b\x32*.protos.playbooks.PlaybookStepExecutionLog\"^\n\x12RunPlaybookRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12,\n\x08playbook\x18\x02 \x01(\x0b\x32\x1a.protos.playbooks.Playbook\"\xc1\x01\n\x13RunPlaybookResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12?\n\x12playbook_execution\x18\x04 \x01(\x0b\x32#.protos.playbooks.PlaybookExecution\"G\n\x13GetPlaybooksRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x14\n\x0cplaybook_ids\x18\x02 \x03(\x04\"a\n\x14GetPlaybooksResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12-\n\tplaybooks\x18\x02 \x03(\x0b\x32\x1a.protos.playbooks.Playbook\"S\n\x15\x43reatePlaybookRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x08playbook\x18\x02 \x01(\x0b\x32\x1a.protos.playbooks.Playbook\"\x95\x01\n\x16\x43reatePlaybookResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12,\n\x08playbook\x18\x03 \x01(\x0b\x32\x1a.protos.playbooks.Playbook\"\x8b\x01\n\x15UpdatePlaybookRequest\x12\x31\n\x0bplaybook_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12?\n\x13update_playbook_ops\x18\x02 \x03(\x0b\x32\".protos.playbooks.UpdatePlaybookOp\"g\n\x16UpdatePlaybookResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"g\n\x16\x45xecutePlaybookRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x31\n\x0bplaybook_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"\xbb\x01\n\x17\x45xecutePlaybookResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12\x35\n\x0fplaybook_run_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"p\n\x1b\x45xecutionPlaybookGetRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x35\n\x0fplaybook_run_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xca\x01\n\x1c\x45xecutionPlaybookGetResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12?\n\x12playbook_execution\x18\x04 \x01(\x0b\x32#.protos.playbooks.PlaybookExecution\"\xce\x01\n\x1f\x45xecutionPlaybookAPIGetResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12@\n\x13playbook_executions\x18\x04 \x03(\x0b\x32#.protos.playbooks.PlaybookExecution\"R\n\x1e\x45xecutionsPlaybooksListRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x14\n\x0cplaybook_ids\x18\x02 \x03(\t\"\xce\x01\n\x1f\x45xecutionsPlaybooksListResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12@\n\x13playbook_executions\x18\x04 \x03(\x0b\x32#.protos.playbooks.PlaybookExecution\"\x94\x01\n\x1cPlaybookTemplatesGetResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12%\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Struct\"G\n\x13GetWorkflowsRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x14\n\x0cworkflow_ids\x18\x02 \x03(\x04\"a\n\x14GetWorkflowsResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12-\n\tworkflows\x18\x02 \x03(\x0b\x32\x1a.protos.playbooks.Workflow\"S\n\x15\x43reateWorkflowRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x08workflow\x18\x02 \x01(\x0b\x32\x1a.protos.playbooks.Workflow\"\x95\x01\n\x16\x43reateWorkflowResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12,\n\x08workflow\x18\x03 \x01(\x0b\x32\x1a.protos.playbooks.Workflow\"\x8b\x01\n\x15UpdateWorkflowRequest\x12\x31\n\x0bworkflow_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12?\n\x13update_workflow_ops\x18\x02 \x03(\x0b\x32\".protos.playbooks.UpdateWorkflowOp\"g\n\x16UpdateWorkflowResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"\x9c\x01\n\x16\x45xecuteWorkflowRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x31\n\x0bworkflow_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x33\n\rworkflow_name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xbb\x01\n\x17\x45xecuteWorkflowResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12\x35\n\x0fworkflow_run_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"p\n\x1b\x45xecutionWorkflowGetRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x35\n\x0fworkflow_run_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xcb\x01\n\x1c\x45xecutionWorkflowGetResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12@\n\x13workflow_executions\x18\x04 \x03(\x0b\x32#.protos.playbooks.WorkflowExecution\"R\n\x1e\x45xecutionsWorkflowsListRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12\x14\n\x0cworkflow_ids\x18\x02 \x03(\t\"\xce\x01\n\x1f\x45xecutionsWorkflowsListResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12+\n\x07success\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0f.protos.Message\x12@\n\x13workflow_executions\x18\x04 \x03(\x0b\x32#.protos.playbooks.WorkflowExecutionb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RUNPLAYBOOKTASKREQUEST._serialized_start=251
  _RUNPLAYBOOKTASKREQUEST._serialized_end=379
  _RUNPLAYBOOKTASKRESPONSE._serialized_start=382
  _RUNPLAYBOOKTASKRESPONSE._serialized_end=592
  _RUNPLAYBOOKTASKRESPONSEV2._serialized_start=595
  _RUNPLAYBOOKTASKRESPONSEV2._serialized_end=797
  _RUNPLAYBOOKSTEPREQUEST._serialized_start=799
  _RUNPLAYBOOKSTEPREQUEST._serialized_end=916
  _RUNPLAYBOOKSTEPRESPONSE._serialized_start=919
  _RUNPLAYBOOKSTEPRESPONSE._serialized_end=1225
  _RUNPLAYBOOKSTEPRESPONSEV2._serialized_start=1228
  _RUNPLAYBOOKSTEPRESPONSEV2._serialized_end=1434
  _RUNPLAYBOOKREQUEST._serialized_start=1436
  _RUNPLAYBOOKREQUEST._serialized_end=1530
  _RUNPLAYBOOKRESPONSE._serialized_start=1533
  _RUNPLAYBOOKRESPONSE._serialized_end=1726
  _GETPLAYBOOKSREQUEST._serialized_start=1728
  _GETPLAYBOOKSREQUEST._serialized_end=1799
  _GETPLAYBOOKSRESPONSE._serialized_start=1801
  _GETPLAYBOOKSRESPONSE._serialized_end=1898
  _CREATEPLAYBOOKREQUEST._serialized_start=1900
  _CREATEPLAYBOOKREQUEST._serialized_end=1983
  _CREATEPLAYBOOKRESPONSE._serialized_start=1986
  _CREATEPLAYBOOKRESPONSE._serialized_end=2135
  _UPDATEPLAYBOOKREQUEST._serialized_start=2138
  _UPDATEPLAYBOOKREQUEST._serialized_end=2277
  _UPDATEPLAYBOOKRESPONSE._serialized_start=2279
  _UPDATEPLAYBOOKRESPONSE._serialized_end=2382
  _EXECUTEPLAYBOOKREQUEST._serialized_start=2384
  _EXECUTEPLAYBOOKREQUEST._serialized_end=2487
  _EXECUTEPLAYBOOKRESPONSE._serialized_start=2490
  _EXECUTEPLAYBOOKRESPONSE._serialized_end=2677
  _EXECUTIONPLAYBOOKGETREQUEST._serialized_start=2679
  _EXECUTIONPLAYBOOKGETREQUEST._serialized_end=2791
  _EXECUTIONPLAYBOOKGETRESPONSE._serialized_start=2794
  _EXECUTIONPLAYBOOKGETRESPONSE._serialized_end=2996
  _EXECUTIONPLAYBOOKAPIGETRESPONSE._serialized_start=2999
  _EXECUTIONPLAYBOOKAPIGETRESPONSE._serialized_end=3205
  _EXECUTIONSPLAYBOOKSLISTREQUEST._serialized_start=3207
  _EXECUTIONSPLAYBOOKSLISTREQUEST._serialized_end=3289
  _EXECUTIONSPLAYBOOKSLISTRESPONSE._serialized_start=3292
  _EXECUTIONSPLAYBOOKSLISTRESPONSE._serialized_end=3498
  _PLAYBOOKTEMPLATESGETRESPONSE._serialized_start=3501
  _PLAYBOOKTEMPLATESGETRESPONSE._serialized_end=3649
  _GETWORKFLOWSREQUEST._serialized_start=3651
  _GETWORKFLOWSREQUEST._serialized_end=3722
  _GETWORKFLOWSRESPONSE._serialized_start=3724
  _GETWORKFLOWSRESPONSE._serialized_end=3821
  _CREATEWORKFLOWREQUEST._serialized_start=3823
  _CREATEWORKFLOWREQUEST._serialized_end=3906
  _CREATEWORKFLOWRESPONSE._serialized_start=3909
  _CREATEWORKFLOWRESPONSE._serialized_end=4058
  _UPDATEWORKFLOWREQUEST._serialized_start=4061
  _UPDATEWORKFLOWREQUEST._serialized_end=4200
  _UPDATEWORKFLOWRESPONSE._serialized_start=4202
  _UPDATEWORKFLOWRESPONSE._serialized_end=4305
  _EXECUTEWORKFLOWREQUEST._serialized_start=4308
  _EXECUTEWORKFLOWREQUEST._serialized_end=4464
  _EXECUTEWORKFLOWRESPONSE._serialized_start=4467
  _EXECUTEWORKFLOWRESPONSE._serialized_end=4654
  _EXECUTIONWORKFLOWGETREQUEST._serialized_start=4656
  _EXECUTIONWORKFLOWGETREQUEST._serialized_end=4768
  _EXECUTIONWORKFLOWGETRESPONSE._serialized_start=4771
  _EXECUTIONWORKFLOWGETRESPONSE._serialized_end=4974
  _EXECUTIONSWORKFLOWSLISTREQUEST._serialized_start=4976
  _EXECUTIONSWORKFLOWSLISTREQUEST._serialized_end=5058
  _EXECUTIONSWORKFLOWSLISTRESPONSE._serialized_start=5061
  _EXECUTIONSWORKFLOWSLISTRESPONSE._serialized_end=5267
# @@protoc_insertion_point(module_scope)
