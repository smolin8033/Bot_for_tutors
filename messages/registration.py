from loader import bot


async def registration_status(telegram_id, response_status):
    if response_status == 201:
        message = "You have been successfully registered!"
        await bot.send_message(telegram_id, f"Your user id is: {telegram_id}")
    else:
        message = "The registration failed. You have probably been already registered before."
    await bot.send_message(telegram_id, message)
