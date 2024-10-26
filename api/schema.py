from pydantic import BaseModel, Field


class Instance(BaseModel):
    id: str = Field(description="Unique identifier of instance")
    url: str = Field(description="Ingestion endpoint of the instance")
