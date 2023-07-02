from commands.task import student_commands, teacher_commands
from entities import User
from loader import bot, dp


@dp.message_handler(commands=["get_commands"])
async def get_commands(user: User) -> None:
    await bot.send_message(user.telegram_id, "Here is the list of all commands, available to you:")

    if user.role == "teacher":
        await bot.send_message(user.telegram_id, "\n".join(teacher_commands))
    elif user.role == "student":
        await bot.send_message(user.telegram_id, "\n".join(student_commands))
