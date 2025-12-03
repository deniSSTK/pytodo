from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User


class AuthRepo:
    async def get_user_by_email(self, session: AsyncSession, email: str) -> User | None:
        result = await session.execute(select(User).where(User.email == email))
        return result.scalars().first()

auth_repo = AuthRepo()