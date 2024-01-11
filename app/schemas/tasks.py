from pydantic import BaseModel
from datetime import datetime
from typing import List


class TaskSchema(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    attachments: List[str]

    class Config:
        from_attributes = True


class SignUpRequest(BaseModel):
    name: str
    description: str
    attachments: List[str]


class TaskUpdateRequest(BaseModel):
    name: str
    description: str
    attachments: List[str]


class TasksListResponse(BaseModel):
    tasks: List[TaskSchema]


class TaskDetailResponse(BaseModel):
    task: TaskSchema
