from pydantic import BaseModel


class KafkaMessage(BaseModel):
    data: str
