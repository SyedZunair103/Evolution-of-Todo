# Data Model

## SQLModel Classes

```python
from sqlmodel import SQLModel, Field, create_engine, Session
from datetime import datetime
from typing import Optional

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Task(TaskBase, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TaskCreate(TaskBase):
    pass

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskPublic(TaskBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
```

## Neon Environment Variables
- `DATABASE_URL`: Connection string for Neon PostgreSQL
- `SQLALCHEMY_DATABASE_URL`: Same as DATABASE_URL for compatibility

## Initial Schema Notes
- Foreign key relationship between Task and User
- Indexes on user_id for efficient querying
- Timestamps for audit trail
- Unique constraint on user email