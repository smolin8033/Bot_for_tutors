from dataclasses import dataclass
from typing import Optional


@dataclass
class Hometask:
    name: str
    start_datetime: str
    end_datetime: str
    coursebook: Optional[str]
    exercises: Optional[str]
    url: Optional[str]
    more_info: Optional[str]


hometask = Hometask(
    name="",
    start_datetime="",
    end_datetime="",
    coursebook="",
    exercises="",
    url="",
    more_info="",
)
