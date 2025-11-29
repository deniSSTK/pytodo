from sqlalchemy import Column, String, UUID, ForeignKey, Text
from sqlalchemy.orm import relationship

from core.database import Base
from models.base import BaseModelMixin


class Task(Base, BaseModelMixin):
    __tablename__ = "tasks"

    creator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(Text)

    creator = relationship("User")