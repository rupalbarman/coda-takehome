from abc import abstractmethod
from typing import Any


class Repository(object):
    def __init__(self, url: str) -> None:
        self.url = url
        self.client: Any | None = None

    @abstractmethod
    async def connect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def disconnect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get(self, key: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_by_pattern(self, pattern: str) -> list[Any]:
        raise NotImplementedError

    @abstractmethod
    async def put(self, key: str, value: str, **kwargs) -> Any | None:
        raise NotImplementedError
