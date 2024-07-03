import json
import logging

from google.protobuf.wrappers_pb2 import StringValue

from connectors.crud.connectors_crud import get_db_connectors, get_db_account_connector_keys
from connectors.models import integrations_connector_type_display_name_map
from executor.source_processors.openai_api_processor import OpenAiApiProcessor
from intelligence_layer.result_interpreters.result_interpreter import ResultInterpreter
from intelligence_layer.utils import generate_graph_for_timeseries_result

from media.utils import generate_local_image_path
from protos.base_pb2 import Source as ConnectorType, SourceKeyType, Source
from protos.playbooks.intelligence_layer.interpreter_pb2 import Interpretation as InterpretationProto, InterpreterType, \
    Interpretation
from protos.playbooks.playbook_commons_pb2 import PlaybookTaskResult, PlaybookTaskResultType, TimeseriesResult

logger = logging.getLogger(__name__)


def get_task_result_data_type(task_result: PlaybookTaskResult):
    if task_result.type == PlaybookTaskResultType.TIMESERIES:
        return 'metric'
    else:
        return ''


def gpt_metric_task_prompts(generated_image_url: str):
    keys = """
        anomaly_detected:boolean
        description:string
    """

    system_prompt = """
                    You are a DevOps engineer who is an expert at reading metrics graphs. These metrics are 
                    generated by tools and services that you use to deploy and monitor your applications or services.
                    You are responsible for reading the metrics and detecting if there is any anomaly here.
                    You will be given an image of the metrics data. You will need to return a JSON object with the 
                    following keys:
                    {keys}
        """.format(keys=keys)

    gpt_prompt = [
        {
            "type": "text",
            "text": "This image is of and identify if you find any anomaly. If you do, describe the issue. Only send "
                    "the keys that are requested. Do not send more keys or keys with empty or N/A values. Strictly "
                    "do not respond with empty strings or N/A or 'No Data' as key values."
        },
        {
            "type": "image_url",
            "image_url": {
                "url": generated_image_url,
            },
        },
    ]
    return system_prompt, gpt_prompt


def vision_api_evaluation_function(open_ai_api_key, data_type, image_url: str):
    if data_type == 'metric':
        try:
            system_prompt, gpt_prompt = gpt_metric_task_prompts(image_url)
        except Exception as e:
            logger.error(f'Error getting GPT response: {e}')
            raise e
    # elif data_type == 'logs':
    #     inference_df = pd.DataFrame(columns=['anomaly_detected', 'description', 'additional_data'])
    #
    # elif data_type == 'db_query':
    #     inference_df = pd.DataFrame(columns=['anomaly_detected', 'description', 'additional_data'])
    #
    # elif data_type == 'deployments':
    #     inference_df = pd.DataFrame(columns=['anomaly_detected', 'description', 'additional_data'])
    #
    # elif data_type == 'container_logs':
    #     inference_df = pd.DataFrame(columns=['anomaly_detected', 'description', 'additional_data'])
    else:
        logger.error(f'Unsupported data type: {data_type}')
        raise NotImplementedError(f'Unsupported data type: {data_type}')
    open_ai_processor = OpenAiApiProcessor(open_ai_api_key=open_ai_api_key)
    gpt_response = open_ai_processor.chat_completions_create(
        model="gpt-4-turbo",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": gpt_prompt}
        ]
    )
    logger.info(gpt_response.choices[0])
    logger.info(gpt_response.choices[0].message.content)
    gpt_response = gpt_response.choices[0].message.content
    gpt_response = json.loads(gpt_response)
    return {'anomaly_detected': gpt_response['anomaly_detected'], 'description': gpt_response['description']}


class LlmChatGptVisionResultInterpreter(ResultInterpreter):
    def __init__(self):
        self.type = InterpreterType.LLM_CHAT_GPT_VISION_I

    def interpret(self, task_result: PlaybookTaskResult):
        open_ai_integration = get_db_connectors(connector_type=ConnectorType.OPEN_AI, is_active=True)
        if not open_ai_integration:
            raise ValueError('OpenAI integration is not set.')
        open_ai_integration = open_ai_integration.first()
        open_ai_api_key = get_db_account_connector_keys(open_ai_integration.account, open_ai_integration.id,
                                                        key_type=SourceKeyType.OPEN_AI_API_KEY)
        if not open_ai_api_key:
            raise ValueError('OpenAI API key is not set.')
        open_ai_api_key = open_ai_api_key.first().key

        result_type = task_result.type
        data_type = get_task_result_data_type(task_result)
        if data_type == 'metric':
            try:
                timeseries_result: TimeseriesResult = task_result.timeseries
                file_key = generate_local_image_path()
                metric_expression = timeseries_result.metric_expression.value
                metric_expression = metric_expression.replace('`', '')
                metric_name = timeseries_result.metric_name.value
                metric_source = integrations_connector_type_display_name_map.get(task_result.source,
                                                                                 Source.Name(task_result.source))
                object_url = generate_graph_for_timeseries_result(timeseries_result, file_key, metric_expression)
                if not object_url:
                    return Interpretation()
                inference = vision_api_evaluation_function(open_ai_api_key, data_type, object_url)
                if not inference or inference is None:
                    raise ValueError('No inference returned from chat gpt')
                title = f'Fetched `{metric_expression}` for `{metric_name}` from `{metric_source}`'
                description = f'`Description`: {inference["description"]}'
                summary = f'`Anomaly Detected`: {inference["anomaly_detected"]}'

                return InterpretationProto(
                    type=InterpretationProto.Type.IMAGE,
                    interpreter_type=self.type,
                    title=StringValue(value=title),
                    description=StringValue(value=description),
                    summary=StringValue(value=summary),
                    image_url=StringValue(value=object_url),
                    model_type = Interpretation.ModelType.PLAYBOOK_TASK
                )
            except Exception as e:
                logger.error(f'Error writing image: {e}')
                return Interpretation()
        else:
            logger.error(f'Unsupported result type: {result_type}')
            return Interpretation()


llm_chat_gpt_vision_result_interpreter = LlmChatGptVisionResultInterpreter()
