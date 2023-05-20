import logging

from pydantic import BaseSettings

from config.logging_conf.loggers import logger

for handler in logger.handlers:
    handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))


class Settings(BaseSettings):
    TOKEN: str
    WEB_SERVICE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
