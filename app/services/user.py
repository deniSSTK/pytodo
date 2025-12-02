from fastapi.openapi.models import Response
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from repositories.user import user_repo
from schemas.auth import AuthUser
from schemas.user import UserCreate
from utils.cookies import set_cookie, COOKIE_REFRESH
from utils.security.jwt_provider import jwt_provider
from utils.security.hash_password import hash_password


class UserService:
    async def get_user(self, session: AsyncSession, user_id: str):
        return await user_repo.get_user(session, user_id)

    async def create_user(self, session: AsyncSession, response: Response, dto: UserCreate) -> AuthUser:
        user = User(
            name=dto.name,
            email=str(dto.email),
            password_hash=hash_password(dto.password),
        )

        created_user = await user_repo.create_user(session, user)

        jwt_data = {
            "id": str(created_user.id),
        }

        access_token = jwt_provider.create_access_token(jwt_data)
        refresh_token = jwt_provider.create_refresh_token(jwt_data)

        set_cookie(response, COOKIE_REFRESH, refresh_token)

        return AuthUser(
            id=created_user.id,
            access_token=access_token,
        )
        

user_service = UserService()