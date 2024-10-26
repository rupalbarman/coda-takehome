from pydantic import Field, RedisDsn
from pydantic_core import Url
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    REDIS_URL: RedisDsn = Field(default="redis://redis:6379/0")
    HEARTBEAT_URL: Url = Field(default="http://localhost:8001/beat/")
    INGESTION_URL: Url = Field(default="http://localhost:8001/api/")
    HEARTBEAT_SEC: int = Field(default=30)

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)


settings = Settings()
