from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator
from app.models import TaskStatus, TaskPriority

class TaskCreate(BaseModel):
    title: str = Field(..., max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: Optional[TaskStatus] = TaskStatus.pending
    priority: Optional[TaskPriority] = TaskPriority.medium
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = Field(default=None, max_length=100)

    @validator('title')
    def title_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Title cannot be empty or whitespace")
        return v.strip()

    @validator('due_date')
    def due_date_in_future(cls, v):
        if v and v <= datetime.utcnow():
            raise ValueError("Due date must be in the future")
        return v

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TaskStatus]
    priority: Optional[TaskPriority]
    due_date: Optional[datetime]
    assigned_to: Optional[str] = Field(None, max_length=100)

    @validator('title')
    def title_not_empty(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Title cannot be empty or whitespace")
        return v.strip()

    @validator('due_date')
    def due_date_in_future(cls, v):
        if v and v <= datetime.utcnow():
            raise ValueError("Due date must be in the future")
        return v

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: Optional[datetime]
    due_date: Optional[datetime]
    assigned_to: Optional[str]

    model_config = {
        "from_attributes": True
    }
