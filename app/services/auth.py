from fastapi.openapi.models import Response
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.auth import auth_repo
from schemas.auth import AuthUser
from schemas.request.auth_request import AuthRequest
from schemas.response.auth_response import AuthResponse
from utils.cookies import set_cookie
from utils.security.jwt_provider import jwt_provider


class AuthService:
    async def login(self, session: AsyncSession, response: Response, dto: AuthRequest) -> AuthResponse | None:
        user = await auth_repo.get_user_by_email(session, dto.email)
        if not user:
            return None

        from utils.security.hash_password import check_password
        if not check_password(dto.password, user.password_hash):
            return None

        auth_user = AuthUser(
            id=str(user.id),
        )

        access_token = jwt_provider.create_access_token(auth_user)
        refresh_token = jwt_provider.create_refresh_token(auth_user)

        from utils.cookies import COOKIE_REFRESH
        set_cookie(response, COOKIE_REFRESH, refresh_token)

        return AuthResponse(
            access_token=access_token,
            user=auth_user
        )

auth_service = AuthService()