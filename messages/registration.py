from loader import bot

message_mapper = {
    201: "You have been successfully registered",
    400: "You have been registered before",
    403: "You have been registered before",
    500: "Failed to register due to a server problem",
    502: "Failed to register due to a server problem",
}


async def send_registration_status(telegram_id: int, response_status: int) -> None:
    message = message_mapper.get(response_status)
    if message is None:
        message = "The registration failed."
    if response_status == 201:
        await bot.send_message(telegram_id, f"Your user id is {telegram_id}")
    await bot.send_message(telegram_id, message)
    return
