from aiogram import types

from api.registration import http_client
from entities import User
from loader import dp


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi, I will register you. Type: /register")


@dp.message_handler(commands=["register"])
async def register(message: types.Message):
    """
    This handler will be called when user sends `/register` command
    """
    user = User(username=message.from_user.username, telegram_id=message.from_user.id)
    await http_client.registration(user)
    await message.reply(f"Your user id is: {user.telegram_id}")
