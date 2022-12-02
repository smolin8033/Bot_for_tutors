import asyncio

import aiohttp

"""
def send_registration_data(user_id, username):
    url = 'http://localhost/api/telegram_users/'
    data = {
        "username": username,
        "telegram_id": user_id
    }
    result = requests.post(url=url, data=data)
    return result
"""

async def send_registration_data(user_id, username):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost/api/telegram_users/', data={
        "username": username,
        "telegram_id": user_id
    }) as resp:
            print(resp.status)
            print(await resp.text())


asyncio.run(send_registration_data())