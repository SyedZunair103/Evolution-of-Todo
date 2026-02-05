from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    user_id: int
    title: str
    description: str = ""
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class TaskCreateRequest(BaseModel):
    """Schema for creating tasks - user_id comes from URL path"""
    title: str
    description: str = ""
    completed: bool = False


class TaskRead(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskToggleComplete(BaseModel):
    completed: bool