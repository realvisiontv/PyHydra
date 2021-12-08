from typing import Callable

from fastapi import FastAPI
from app.api.dependencies.sink_kafka_dep import AIOProducer, Producer
from app.core import config


def get_kafka_config():
    settings = config.get_app_settings()
    kconf = {"bootstrap.servers": settings.BOOTSTRAP_SERVERS,
             "security.protocol": settings.SECURITY_PROTOCOL,
             "sasl.mechanisms": settings.SASL_MECHANISMS,
             "sasl.username": settings.SASL_USERNAME,
             "sasl.password": settings.SASL_PASSWORD,
             }
    return kconf


config = get_kafka_config()
producer = None
aio_producer = None


async def startup_event() -> None:
    global producer, aio_producer
    aio_producer = AIOProducer(config)
    producer = Producer(config)


def shutdown_event() -> None:
    aio_producer.close()
    producer.close()


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    return startup_event


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    return shutdown_event

