from confluent_kafka import KafkaException, Message
from fastapi import APIRouter, HTTPException

from app.core import events
from app.models.domain import KafkaMessage

router = APIRouter()


@router.post("/topic/{topic}")
async def send_msg(topic: str, msg: KafkaMessage):
    try:
        result: Message = await events.aio_producer.produce(topic, msg.data)
        return {
            "timestamp": result.timestamp(),
            "ack": {
                "key": result.key(),
                "topic": result.topic(),
                "partition": result.partition(),
                "offset": result.offset(),
            },
        }
    except KafkaException as ex:
        raise HTTPException(status_code=500, detail=ex.args[0].str())


@router.get("/topic")
async def get_topics(topic: str, msg: KafkaMessage):
    """
    Get all topics
    :param topic:
    :param msg:
    :return:
    """
    pass


@router.get("schema/")
async def get_schemas(topic: str, msg: KafkaMessage):
    """
    Get all schemas
    :param topic:
    :param msg:
    :return:
    """
    pass


@router.post("schema/{schema_name}")
async def create_schema(topic: str, msg: KafkaMessage):
    """
    Create a
    :param topic:
    :param msg:
    :return:
    """
    pass
