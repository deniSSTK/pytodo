from sqlalchemy.ext.asyncio import AsyncSession

from models.task import Task


class TaskRepo:
    async def create_task(self, session: AsyncSession, task: Task):
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task

task_repo = TaskRepo()