import asyncio.exceptions
from dataclasses import asdict

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

    async def request(self, name="get", **kwargs) -> None | ClientResponse:
        async with ClientSession(timeout=ClientTimeout(total=self.timeout)) as session:
            try:
                async with getattr(session, name)(self.url, **kwargs) as response:
                    ...
            except asyncio.TimeoutError as exc:
                logger.error(type(exc))
            except ClientConnectionError as exc:
                logger.error(f"{type(exc)}: {exc}")
                return
            return response

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

        if response is None:
            logger.error("Failed to get response")

        if response:

            if not response.ok:
                logger.error(f"{response.status} {response.json()}")

            if response.status == 201:
                logger.info(
                    f"The user {user.username} (telegram id: {user.telegram_id}) has been successfully registered."
                )

            await send_registration_status(user.telegram_id, response.status)

        return bool(response)

    async def get_users(self):
        response: ClientResponse | None = await self.method(name="get")
        logger.info(f"Response:{response}")

        return response


http_client = HttpClient()
