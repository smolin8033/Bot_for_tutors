from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    username: str
    telegram_id: int
    role: str
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""


user = User(
    username="",
    telegram_id=0,
    role="",
    first_name="",
    last_name="",
)
