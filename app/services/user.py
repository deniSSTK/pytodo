from fastapi.openapi.models import Response
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from repositories.user import user_repo
from schemas.auth import AuthUser
from schemas.response.auth_response import AuthResponse
from schemas.user import UserCreate
from utils.cookies import set_cookie, COOKIE_REFRESH
from utils.security.jwt_provider import jwt_provider
from utils.security.hash_password import hash_password


class UserService:
    async def get_user(self, session: AsyncSession, user_id: str):
        return await user_repo.get_user(session, user_id)

    async def create_user(self, session: AsyncSession, response: Response, dto: UserCreate) -> AuthResponse:
        user = User(
            name=dto.name,
            email=str(dto.email),
            password_hash=hash_password(dto.password),
        )

        created_user = await user_repo.create_user(session, user)

        auth_user = AuthUser(
            id=str(created_user.id),
        )

        refresh_token = jwt_provider.create_refresh_token(auth_user)
        access_token = jwt_provider.create_access_token(auth_user)

        set_cookie(response, COOKIE_REFRESH, refresh_token)

        return AuthResponse(
            user=auth_user,
            access_token=access_token,
        )
        

user_service = UserService()