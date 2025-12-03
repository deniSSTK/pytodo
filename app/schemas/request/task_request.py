from typing import Optional

from pydantic import BaseModel


class TaskCreateRequest(BaseModel):
    title: str
    description: Optional[str] = None