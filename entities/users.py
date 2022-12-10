from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    username: str
    telegram_id: int
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
