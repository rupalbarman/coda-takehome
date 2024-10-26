from typing import Any

from core.repository import Repository


class MemoryRepository(Repository):
    def __init__(self, url: str) -> None:
        super().__init__(url)

    async def connect(self) -> None:
        self.client = {}

    async def disconnect(self) -> None:
        if isinstance(self.client, dict):
            self.client.clear()

    async def get(self, key: str) -> Any:
        return self.client.get(key)

    async def get_by_pattern(self, pattern: str) -> list[Any]:
        values = []
        for key, value in self.client.items():
            if key.startswith(pattern):
                values.append(value)

        return values

    async def put(self, key: str, value: str, **kwargs) -> Any | None:
        self.client[key] = value


memory = MemoryRepository(url="memory")
