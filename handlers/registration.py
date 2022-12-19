from aiogram import types

from api.registration import http_client
from entities import User
from keyboards.inline_keyboards import inline_keyboard
from loader import bot, dp


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi, I will register you. Type: /register")


@dp.message_handler(commands=["register"])
async def ask_about_role(message: types.Message):
    await message.reply("Are you a teacher or a student?", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda callback_query: "teacher" or "student" in callback_query.data)
async def process_callback(callback_query: types.CallbackQuery):
    role: str = callback_query.data.split(":")[-1]
    await callback_query.answer("Your choice is accepted")
    await bot.send_message(callback_query.from_user.id, f"You will be registered as a {role}")
    await register(callback_query, role)


async def register(callback_query: types.CallbackQuery, role: str):
    user = User(
        username=callback_query.from_user.username,
        telegram_id=callback_query.from_user.id,
        first_name=callback_query.from_user.first_name,
        last_name=callback_query.from_user.last_name,
        role=role,
    )
    await http_client.registration(user)
