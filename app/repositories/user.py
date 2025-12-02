from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from sqlalchemy.future import select

class UserRepo:
    async def get_user(self, session: AsyncSession, user_id: str):
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalars().first()

    async def create_user(self, session: AsyncSession, user: User):
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

user_repo = UserRepo()