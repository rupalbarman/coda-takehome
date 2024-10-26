from pydantic import Field, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    REDIS_URL: RedisDsn = Field(default="redis://redis:6379/0")
    HEARTBEAT_SEC: int = Field(default=30)
    INSTANCES: list[str] = []

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)


settings = Settings()
