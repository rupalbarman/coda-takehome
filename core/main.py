import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response

from core.config import settings
from core.repository.redis import redis
from core.schema import Instance
from core.task import update_instances


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Core has started")
    await redis.connect()
    asyncio.create_task(update_instances(redis))
    yield
    await redis.disconnect()
    print("Core has started")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "I'm Core"}


@app.post("/beat/")
async def beat(request: Request):
    print("Core received heartbeat")
    try:
        json = await request.json()
        instance = Instance.model_validate_json(json)
    except Exception as e:
        print(e)
        return Response(status_code=400)

    instance_key = f"instance-{instance.id}"
    await redis.put(
        key=instance_key,
        value=instance.url,
        expires_in_sec=settings.HEARTBEAT_SEC,
    )
    return Response(status_code=200)


@app.get("/all")
async def instances():
    return {"message": settings.INSTANCES}
