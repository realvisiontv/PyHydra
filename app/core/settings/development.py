import logging
import os

from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Development PyHydra"

    logging_level: int = logging.DEBUG

