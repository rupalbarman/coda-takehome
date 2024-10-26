from typing import Any

from redis.asyncio import Redis

from core.config import settings
from core.repository import Repository


class RedisRepository(Repository):
    def __init__(self, url: str) -> None:
        super().__init__(url)

    async def connect(self) -> None:
        self.client = Redis.from_url(self.url)

    async def disconnect(self) -> None:
        if self.client is not None:
            await self.client.aclose()

    async def get(self, key: str) -> Any:
        value = await self.client.get(key)
        value = value.decode("utf-8")
        return value

    async def get_by_pattern(self, pattern: str) -> list[Any]:
        values = []
        pattern = f"{pattern}*"
        async for key in self.client.scan_iter(pattern):
            value = await self.get(key=key)
            values.append(value)

        return values

    async def put(
        self,
        key: str,
        value: str,
        expires_in_sec: int | None = None,
    ) -> None:
        await self.client.set(key, value, ex=expires_in_sec)


redis = RedisRepository(url=str(settings.REDIS_URL))
