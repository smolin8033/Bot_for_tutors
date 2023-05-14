import asyncio.exceptions
from dataclasses import asdict
from typing import Tuple

from aiohttp import ClientResponse, ClientSession, ClientTimeout
from aiohttp.client_exceptions import ClientConnectionError

from api.constants import USER_AGENT
from config.conf import logger, settings
from entities import User
from messages.registration import send_registration_status


class HttpClient:
    def __init__(self):
        self.timeout = 60
        self.url = settings.WEB_SERVICE_URL
        self.headers = {
            "User-Agent": USER_AGENT,
        }

    async def request(self, name="get", **kwargs) -> Tuple[None | ClientResponse, None | str] | None:
        async with ClientSession(timeout=ClientTimeout(total=self.timeout)) as session:
            try:
                async with getattr(session, name)(self.url, **kwargs) as response:
                    response_text = await response.json()
                    ...
            except asyncio.TimeoutError as exc:
                logger.error(type(exc))
            except ClientConnectionError as exc:
                logger.error(f"{type(exc)}: {exc}")
                return
            return response, response_text

    async def method(self, name="get", data: dict = None, headers: dict = None) -> None | ClientResponse:
        kwargs = {"headers": self.headers}
        if data:
            kwargs["data"] = data
        if headers:
            for key, value in headers.items():
                kwargs["headers"].update({key: value})

        response: ClientResponse | None = await self.request(name, **kwargs)
        return response

    async def registration(self, user: User) -> bool:
        response: ClientResponse | None = await self.method(
            name="post",
            data=asdict(user),
            headers={"telegram-id": str(user.telegram_id), "role": user.role, "username": user.username},
        )
        logger.info(f"\n\n in async def registration респонс {response} \n\n")

        if response is None:
            logger.error("Failed to get response")

        if response:

            if not response[0].ok:
                logger.error(f"{response[0].status} {response[0].json()}")

            if response[0].status == 201:
                logger.info(
                    f"The user {user.username} (telegram id: {user.telegram_id}) has been successfully registered."
                )

            await send_registration_status(user.telegram_id, response[0].status)

        return bool(response)

    async def get_users(self) -> str:
        response_tuple: Tuple[None | ClientResponse, None | str] | None = await self.method(
            name="get", headers={"telegram-id": "341861983", "role": "teacher", "username": "alexsm0l"}
        )

        return response_tuple[1]


http_client = HttpClient()
