from aiogram import types

from api.registration import http_client
from config.conf import logger
from entities import User
from keyboards.reply_keyboards import reply_keyboard
from loader import dp


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi, I will register you. Type: /register")


@dp.message_handler(commands=["register"])
@dp.callback_query_handler()
async def register(message: types.Message, callback_data):
    """
    This handler will be called when user sends `/register` command
    """
    user = User(
        username=message.from_user.username,
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    await message.reply("Are you a teacher or a student?", reply_markup=reply_keyboard)
    logger.info(callback_data)
    await http_client.registration(user)
