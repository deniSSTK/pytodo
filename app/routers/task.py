from fastapi import APIRouter, Request, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from dependencies.auth import auth_required
from schemas.request.task_request import TaskCreateRequest
from services.task import task_service

router = APIRouter(prefix="/task", tags=["task"])

@router.post("/", dependencies=[Depends(auth_required)])
async def _create_task(dto: TaskCreateRequest, request: Request, session: AsyncSession = Depends(get_session)):
    await task_service.create_task(session, request, dto)
    return Response(status_code=200)