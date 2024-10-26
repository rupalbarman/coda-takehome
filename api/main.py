import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from api.task import heartbeat


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("API has started")
    asyncio.create_task(heartbeat())
    yield
    print("API has started")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "I'm API"}


@app.post("/api/")
async def api(request: Request):
    json = await request.json()
    print("API got", json)
    return json
