from fastapi import APIRouter, Request

from schemas.auth import AuthToken
from utils.cookies import get_cookie, COOKIE_REFRESH
from utils.security.jwt_provider import jwt_provider

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/refresh/access", response_model=AuthToken)
async def _refresh_access(request: Request):
    refresh_token = get_cookie(request, COOKIE_REFRESH)

    jwt_data = jwt_provider.decode_token(refresh_token)

    access_token = jwt_provider.create_access_token(jwt_data)

    return { "access_token": access_token }