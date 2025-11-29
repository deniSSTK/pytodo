from sqlalchemy import Column, String

from core.database import Base
from models.base import BaseModelMixin


class User(Base, BaseModelMixin):
    __tablename__ = "users"

    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

