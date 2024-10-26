import asyncio

from core.config import settings
from core.repository import Repository


async def update_instances(repo: Repository):
    heartbeat_sec = settings.HEARTBEAT_SEC
    while True:
        print("UPDATING LISTS")
        settings.INSTANCES = await repo.get_by_pattern("instance")
        print(settings.INSTANCES)
        await asyncio.sleep(heartbeat_sec)
