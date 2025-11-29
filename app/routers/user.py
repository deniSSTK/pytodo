from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_session
from schemas.user import UserCreate, UserRead
from models.user import User
from crud.user import create_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
async def create_user_endpoint(user: UserCreate, session: AsyncSession = Depends(get_session)):
    db_user = User(name=user.name, email=user.email, password_hash=user.password)
    return await create_user(session, db_user)
