import os
from enum import Enum
from pathlib import Path
from pydantic import BaseSettings
from app import main


def get_root_dir():
    ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
    return str(ROOT_DIR)


class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.dev

    # Kafka
    BOOTSTRAP_SERVERS: str
    SECURITY_PROTOCOL: str
    SASL_MECHANISMS: str
    SASL_USERNAME: str
    SASL_PASSWORD: str

    # Confluent Cloud Schema Registry
    SCHEMA_REGISTRY_URL: str
    BASIC_AUTH_CREDENTIALS_SOURCE: str
    BASIC_AUTH_USER_INFO: str

    class Config:
        env_file = Path(f"{get_root_dir()}/.env")
        env_file_encoding = 'utf-8'
