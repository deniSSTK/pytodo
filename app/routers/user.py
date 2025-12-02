from fastapi import APIRouter, Depends
from fastapi import Response
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from schemas.auth import AuthUser
from schemas.user import UserCreate, UserRead
from services.user import user_service

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/{user_id}", response_model=UserRead)
async def _get_user(user_id: str, session: AsyncSession = Depends(get_session)):
    return await user_service.get_user(session, user_id)

@router.post("/", response_model=AuthUser)
async def _create_user(
        user: UserCreate,
        response: Response,
        session: AsyncSession = Depends(get_session)
):
    return await user_service.create_user(session, response, user)
