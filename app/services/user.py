from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from repositories.user import user_repo
from schemas.user import UserCreate
from utils.security.hash_password import hash_password


class UserService:
    def __init__(self):
        self.user_repo = user_repo

    async def get_user(self, session: AsyncSession, user_id: str):
        return await self.user_repo.get_user(session, user_id)

    async def create_user(self, session: AsyncSession, dto: UserCreate) -> User:
        user = User(
            name=dto.name,
            email=str(dto.email),
            password_hash=hash_password(dto.password),
        )

        return await self.user_repo.create_user(session, user)

user_service = UserService()