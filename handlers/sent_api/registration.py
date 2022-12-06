import aiohttp

from config.conf import settings

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
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.post(settings.WEB_SERVICE_URL, data={
        "username": username,
        "telegram_id": user_id
    }) as resp:
            print(resp.status)
            print(await resp.text())
