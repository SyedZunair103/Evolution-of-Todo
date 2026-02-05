from typing import List, Optional
from sqlmodel import Session, select
from ..models.task import Task, TaskCreate, TaskUpdate, TaskToggleComplete
from fastapi import HTTPException, status
from ..database.connection import engine
from datetime import datetime, timezone


def get_tasks_by_user_id(user_id: int, db: Session) -> List[Task]:
    """Get all tasks for a specific user"""
    statement = select(Task).where(Task.user_id == user_id)
    tasks = db.exec(statement).all()
    return tasks


def get_task_by_id_and_user(task_id: int, user_id: int, db: Session) -> Optional[Task]:
    """Get a specific task for a specific user"""
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    task = db.exec(statement).first()
    return task


def create_task_for_user(task: TaskCreate, db: Session) -> Task:
    """Create a new task for a user"""
    db_task = Task(
        user_id=task.user_id,
        title=task.title,
        description=task.description,
        completed=task.completed,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task_for_user(task_id: int, user_id: int, task_update: TaskUpdate, db: Session) -> Optional[Task]:
    """Update a task for a specific user"""
    db_task = get_task_by_id_and_user(task_id, user_id, db)
    if not db_task:
        return None

    # Update the task with provided values
    if task_update.title is not None:
        db_task.title = task_update.title
    if task_update.description is not None:
        db_task.description = task_update.description
    if task_update.completed is not None:
        db_task.completed = task_update.completed

    # Update the updated_at timestamp
    db_task.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task_for_user(task_id: int, user_id: int, db: Session) -> bool:
    """Delete a task for a specific user"""
    db_task = get_task_by_id_and_user(task_id, user_id, db)
    if not db_task:
        return False

    db.delete(db_task)
    db.commit()
    return True


def toggle_task_completion(task_id: int, user_id: int, task_toggle: TaskToggleComplete, db: Session) -> Optional[Task]:
    """Toggle completion status of a task for a specific user"""
    db_task = get_task_by_id_and_user(task_id, user_id, db)
    if not db_task:
        return None

    db_task.completed = task_toggle.completed

    # Update the updated_at timestamp
    db_task.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(db_task)
    return db_task