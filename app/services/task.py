from fastapi import Request

from sqlalchemy.ext.asyncio import AsyncSession

from repositories.task import task_repo
from schemas.request.task_request import TaskCreateRequest


class TaskService:
    async def create_task(
            self,
            session: AsyncSession,
            request: Request,
            dto: TaskCreateRequest,
    ):
        from models.task import Task
        task = Task(
            title=dto.title,
            description=dto.description,
            creator_id=request.state.user.id
        )
        await task_repo.create_task(session, task)

task_service = TaskService()