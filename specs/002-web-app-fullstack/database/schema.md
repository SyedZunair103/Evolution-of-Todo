# Database Schema

## SQLModel Definitions

### User Model
```python
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

### Task Model
```python
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(default="")
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

## Schema Notes
- **Primary Keys**: Auto-incrementing integers for both User and Task tables
- **Foreign Key**: Task.user_id references User.id with proper indexing
- **Indexing**: Email field on User table and user_id on Task table for performance
- **Constraints**:
  - User email must be unique
  - Task title must be 1-255 characters
  - Task completed defaults to False
- **Timestamps**: Both models include created_at and updated_at fields
- **Default Values**: Proper defaults for optional fields to prevent null values
- **Relationships**: One-to-many relationship between User and Task (one user to many tasks)