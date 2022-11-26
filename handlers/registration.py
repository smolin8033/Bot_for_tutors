from aiogram import types

from handlers.sent_api.registration import send_registration_data
from loader import dp


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi, I will register you. Type: /register")


@dp.message_handler(commands=['register'])
async def register(message: types.Message):
    """
    This handler will be called when user sends `/register` command
    """
    user_id = message.from_user.id
    username = message.from_user.username
    send_registration_data(user_id, username)
    await message.reply(f"Your user id is: {user_id}")
