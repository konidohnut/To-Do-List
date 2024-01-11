from datetime import datetime
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

from app.schemas.tasks import TasksListResponse, SignUpRequest, TaskUpdateRequest, TaskDetailResponse
from app.models.tasks import Task as ModelTask


class TaskService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.model = ModelTask

    async def get_all_tasks(self) -> TasksListResponse:
        tasks = TasksListResponse(tasks=(await self.session.execute(select(self.model))).scalars().all())
        return tasks

    async def get_task_by_id(self, task_id: int) -> TaskDetailResponse:
        try:
            task = (await self.session.execute((select(self.model)).filter_by(id=task_id))).scalar_one()
            return task
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Task does not exist")

    async def create_task(self, task: SignUpRequest) -> SignUpRequest:
        task = ModelTask(name=task.name,
                         description=task.description,
                         created_at=datetime.utcnow(),
                         updated_at=datetime.utcnow(),
                         attachments=task.attachments)
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def update_task(self, task_id_update: int, task_update_request: TaskUpdateRequest) -> TaskUpdateRequest:
        task_db = await self.get_task_by_id(task_id_update)
        task_db.name = task_update_request.name
        task_db.description = task_update_request.description
        task_db.updated_at = datetime.utcnow()
        task_db.attachments = task_update_request.attachments
        await self.session.commit()
        await self.session.refresh(task_db)
        return task_db

    async def remove_task(self, task_id: int):
        task_db = await self.get_task_by_id(task_id)
        await self.session.delete(task_db)
        await self.session.commit()
        return HTTPException(status_code=200, detail="Success delete task")
