from aiogram import Bot, Dispatcher
from config import conf

bot = Bot(token=conf.API_TOKEN)
dp = Dispatcher(bot)