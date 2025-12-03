from sqlalchemy import Column, String

from core.database import Base
from models.base import BaseModelMixin


class User(Base, BaseModelMixin):
    __tablename__ = "users"

    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

