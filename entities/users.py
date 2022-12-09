from dataclasses import dataclass


@dataclass
class User:
    username: str
    telegram_id: int
