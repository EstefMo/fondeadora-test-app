from dataclasses import dataclass

from typing import Any


@dataclass
class Response:
    status: int
    message: str
    data: Any = None
    errors: str = None
