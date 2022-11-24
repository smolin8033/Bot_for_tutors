import logging

from dotenv import dotenv_values

credentials = dotenv_values(".env")

API_TOKEN = credentials["TELEGRAM_TOKEN"]

logging.basicConfig(level=logging.INFO)