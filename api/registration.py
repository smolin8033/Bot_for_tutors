from dataclasses import asdict

import aiohttp

from config.conf import logger, settings
from config.core import USER_AGENT
from entities import User
from messages.registration import registration_status


class HttpClient:
    def __init__(self):
        self.timeout = 60
        self.url = settings.WEB_SERVICE_URL
        self.headers = {
            "User-Agent": USER_AGENT,
        }
        self.data = None

    async def method(self, name="get", data: dict = None, headers: dict = None):
        kwargs = {"headers": self.headers}
        if data:
            self.data = data
        if headers:
            kwargs["headers"] = kwargs["headers"].update(headers)

        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=self.timeout)) as session:
            async with getattr(session, name)(self.url, data=data, **kwargs) as response:
                if response.status == 201:
                    logger.info(
                        f'The user {data["username"]} (telegram id: {data["telegram_id"]}) has been successfully '
                        f"registered."
                    )
                    await registration_status(data["telegram_id"], response.status)
                    return response.ok
                else:
                    logger.error(response.status)
                    await registration_status(data["telegram_id"], response.status)
                    return response.status

    async def registration(self, user: User) -> dict:
        response: dict = await self.method(name="post", data=asdict(user))
        return response


http_client = HttpClient()

"""

async def send_registration_data(user: User):
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.post(settings.WEB_SERVICE_URL, data=asdict(user)) as resp:
            print(resp.status)
            print(await resp.text())
"""
