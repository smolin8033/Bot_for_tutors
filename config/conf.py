import logging

from pydantic import BaseSettings
from pydantic.env_settings import DotenvType

from config.logging_conf.loggers import logger

for handler in logger.handlers:
    handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))


class Settings(BaseSettings):
    TOKEN: str = "TOKEN"
    WEB_SERVICE_URL: str = "WEB_SERVICE_URL"

    class Config:
        env_file: DotenvType = ".env"


settings = Settings()
