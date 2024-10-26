import asyncio
from uuid import uuid4

import aiohttp

from api.config import settings
from api.schema import Instance


async def heartbeat():
    heartbeat_sec = settings.HEARTBEAT_SEC
    heartbeat_url = str(settings.HEARTBEAT_URL)
    ingestion_url = str(settings.INGESTION_URL)

    instance = Instance(id=str(uuid4()), url=ingestion_url)

    async with aiohttp.ClientSession() as session:
        while True:
            instance_json = instance.model_dump_json()
            print("Sending heartbeat with info", instance_json)
            await session.post(url=heartbeat_url, json=instance_json)
            await asyncio.sleep(heartbeat_sec)
