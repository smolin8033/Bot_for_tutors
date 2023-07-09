from dataclasses import asdict

from aiogram import types
from aiogram.utils.exceptions import MessageTextIsEmpty

from api.registration import http_client
from entities.users import user
from faked_data.users_data import faked_user1
from formatters.users import get_first_and_last_name, make_string_representation
from handlers.available_commands import get_commands
from keyboards.inline_keyboards import inline_keyboard
from loader import bot, dp


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message) -> None:
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    user.username = message.from_user.username
    user.telegram_id = message.from_user.id
    user.first_name = message.from_user.first_name
    user.last_name = message.from_user.last_name

    await message.answer("Hi, I will register you. Type: /register")


@dp.message_handler(commands=["register"])
async def ask_about_role(message: types.Message) -> None:
    await message.answer("Are you a teacher or a student?", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda callback_query: "teacher" or "student" in callback_query.data)
async def process_callback(callback_query: types.CallbackQuery) -> None:
    role: str = callback_query.data.split(":")[-1]
    await callback_query.answer("Your choice is accepted")
    await bot.send_message(callback_query.from_user.id, f"You will be registered as a {role}")
    await register(role)


async def register(role: str) -> None:
    user.role = role
    await http_client.send_registration_data(user)
    await get_commands(user)


@dp.message_handler(commands=["get_users"])
async def get_users(message: types.Message) -> None:
    try:
        await message.answer("Here is the list of your teachers/students:")
        users = await http_client.get_users(user)

        names: list = get_first_and_last_name(users)

        users_string_data: str = make_string_representation(names)
        await message.answer(users_string_data)
    except MessageTextIsEmpty:
        await message.answer("No related teachers/students")


@dp.message_handler(commands=["try"])
async def register_test(message: types.Message) -> bool:
    faked_entity = faked_user1
    response: tuple | None = await http_client.method(
        name="post",
        data=asdict(faked_entity),
        headers={
            "telegram-id": str(faked_entity.telegram_id),
            "role": faked_entity.role,
            "username": faked_entity.username,
        },
    )

    return bool(response)
