from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tasks import Task as ModelTask
from app.db.postgres_db import get_db
from app.schemas.tasks import SignUpRequest, TasksListResponse, TaskUpdateRequest, TaskSchema

from app.services.tasks import TaskService

router = APIRouter(tags=["CRUD"])


@router.get("/tasks/", response_model=TasksListResponse)
async def get_tasks(db: AsyncSession = Depends(get_db)):
    task_repo = TaskService(db)
    return await task_repo.get_all_tasks()


@router.get("/{task_id}", response_model=TaskSchema)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = TaskService(db)
    return await task.get_task_by_id(task_id)


@router.post("/create/", response_model=SignUpRequest)
async def create_task_service(task_schema: SignUpRequest,  db: AsyncSession = Depends(get_db)):
    task = TaskService(db)
    return await task.create_task(task_schema)


@router.patch("/update/{task_id}", response_model=TaskUpdateRequest)
async def update_task_endpoint(task_id: int, task_request: TaskUpdateRequest, db: AsyncSession = Depends(get_db)):
    task = TaskService(db)
    return await task.update_task(task_id, task_request)


@router.delete("/delete")
async def delete_task(task_id: int,  db: AsyncSession = Depends(get_db)):
    task = TaskService(db)
    return await task.remove_task(task_id)
