from typing import Any
from dataclasses import dataclass


@dataclass
class Response:
    status: int
    message: str
    data: Any = None
    errors: str = None
