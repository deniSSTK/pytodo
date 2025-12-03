from fastapi import APIRouter, Request, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from schemas.auth import AuthToken
from schemas.request.auth_request import AuthRequest
from schemas.response.auth_response import AuthResponse
from services.auth import auth_service
from utils.cookies import get_cookie, COOKIE_REFRESH
from utils.security.jwt_provider import jwt_provider

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/refresh/access", response_model=AuthToken)
async def _refresh_access(request: Request):
    refresh_token = get_cookie(request, COOKIE_REFRESH)

    auth_user = jwt_provider.decode_token(refresh_token)

    access_token = jwt_provider.create_access_token(auth_user)

    return { "access_token": access_token }

@router.post("/login", response_model=AuthResponse)
async def _login(dto: AuthRequest, response: Response, session: AsyncSession = Depends(get_session)):
    return auth_service.login(response, session, dto)