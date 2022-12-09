import logging

from pydantic import BaseSettings

logging.basicConfig(level=logging.INFO, filemode="w", filename="bot.log")

logger = logging.getLogger()


class Settings(BaseSettings):
    TOKEN: str
    WEB_SERVICE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
