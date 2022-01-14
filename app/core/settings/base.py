from enum import Enum
from pathlib import Path
from typing import Dict, Optional

from pydantic import BaseSettings


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
    SECURITY_PROTOCOL: Optional[str]
    SASL_MECHANISMS: Optional[str]
    SASL_USERNAME: Optional[str]
    SASL_PASSWORD: Optional[str]

    # Confluent Cloud Schema Registry
    SCHEMA_REGISTRY_URL: Optional[str]
    BASIC_AUTH_CREDENTIALS_SOURCE: Optional[str]
    BASIC_AUTH_USER_INFO: Optional[str]

    config_key_map: Dict[str, str] = {
        "BOOTSTRAP_SERVERS": "bootstrap.servers",
        "SECURITY_PROTOCOL": "security.protocol",
        "SASL_MECHANISMS": "sasl.mechanisms",
        "SASL_USERNAME": "sasl.username",
        "SASL_PASSWORD": "sasl.password",
    }

    class Config:
        env_file = Path(f"{get_root_dir()}/.env")
        env_file_encoding = "utf-8"

    def get_kafka_config(self) -> dict:
        final = {}
        for k in self.config_key_map.keys():
            if getattr(self, k):
                final.update({self.config_key_map[k]: getattr(self, k)})
        return final
