from typing import Dict

from google.protobuf.wrappers_pb2 import StringValue

from connectors.utils import generate_credentials_dict
from executor.playbook_source_manager import PlaybookSourceManager
from executor.source_processors.kubectl_api_processor import KubectlApiProcessor
from protos.base_pb2 import Source, TimeRange
from protos.connectors.connector_pb2 import Connector as ConnectorProto
from protos.playbooks.playbook_commons_pb2 import PlaybookTaskResult, PlaybookTaskResultType, BashCommandOutputResult
from protos.playbooks.source_task_definitions.kubectl_task_pb2 import Kubectl


class KubernetesSourceManager(PlaybookSourceManager):

    def __init__(self):
        self.source = Source.KUBERNETES
        self.task_proto = Kubectl
        self.task_type_callable_map = {
            Kubectl.TaskType.COMMAND: {
                'executor': self.execute_command,
                'model_types': [],
                'result_type': PlaybookTaskResultType.BASH_COMMAND_OUTPUT,
                'display_name': 'Trigger a Kubectl Command',
                'category': 'Actions'
            },
        }

    def get_connector_processor(self, kubernetes_connector, **kwargs):
        generated_credentials = generate_credentials_dict(kubernetes_connector.type, kubernetes_connector.keys)
        return KubectlApiProcessor(**generated_credentials)

    def execute_command(self, time_range: TimeRange, global_variable_set: Dict,
                        kubernetes_task: Kubectl, kubernetes_connector: ConnectorProto) -> PlaybookTaskResult:
        try:
            command_str = kubernetes_task.command.command.value
            commands = command_str.split('\n')
            if global_variable_set:
                for key, value in global_variable_set.items():
                    updated_commands = []
                    for command in commands:
                        command = command.replace(f"{{{key}}}", value)
                        updated_commands.append(command)
                    commands = updated_commands
            try:
                outputs = {}
                kubectl_client = self.get_connector_processor(kubernetes_connector)
                for command in commands:
                    command_to_execute = command
                    output = kubectl_client.execute_command(command_to_execute)
                    outputs[command] = output

                command_output_protos = []
                for command, output in outputs.items():
                    bash_command_result = BashCommandOutputResult.CommandOutput(
                        command=StringValue(value=command),
                        output=StringValue(value=output)
                    )
                    command_output_protos.append(bash_command_result)

                return PlaybookTaskResult(
                    source=self.source,
                    type=PlaybookTaskResultType.BASH_COMMAND_OUTPUT,
                    bash_command_output=BashCommandOutputResult(
                        command_outputs=command_output_protos
                    )
                )
            except Exception as e:
                raise Exception(f"Error while executing Kubernetes task: {e}")
        except Exception as e:
            raise Exception(f"Error while executing Kubernetes task: {e}")
