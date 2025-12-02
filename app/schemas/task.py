from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskRead(BaseModel):
    id: UUID
    creator_id: UUID
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
