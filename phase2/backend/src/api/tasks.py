from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session
from ..models.task import Task, TaskCreate as ModelTaskCreate
from ..schemas.task import TaskCreate, TaskRead, TaskUpdate, TaskToggleComplete, TaskCreateRequest
from ..services.task_service import (
    get_tasks_by_user_id,
    get_task_by_id_and_user,
    create_task_for_user,
    update_task_for_user,
    delete_task_for_user,
    toggle_task_completion
)
from ..auth.jwt_validator import get_current_user
from ..logging_config import logger
from ..database.session import get_session

router = APIRouter()


@router.get("/{user_id}/tasks", response_model=List[TaskRead])
def read_tasks(user_id: int, db: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    """
    Retrieve all tasks for a specific user.
    User ID in path must match authenticated user.
    """
    logger.info(f"Fetching tasks for user_id: {user_id}")

    # Verify user_id matches authenticated user
    token_user_id = current_user.get("sub")
    path_user_id = str(user_id)
    logger.info(f"Token user_id: '{token_user_id}' (type: {type(token_user_id)})")
    logger.info(f"Path user_id: '{path_user_id}' (type: {type(path_user_id)})")

    if str(token_user_id) != str(path_user_id):
        logger.warning(f"Unauthorized access attempt to user {path_user_id}'s tasks by user {token_user_id}")
        logger.warning(f"Mismatch: token_user_id='{token_user_id}' vs path_user_id='{path_user_id}'")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to access this user's tasks. Token user: {token_user_id}, Requested user: {path_user_id}"
        )

    tasks = get_tasks_by_user_id(user_id, db)
    logger.info(f"Successfully retrieved {len(tasks)} tasks for user_id: {user_id}")
    return tasks


@router.post("/{user_id}/tasks", response_model=TaskRead)
def create_task(user_id: int, task: TaskCreateRequest, db: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    """
    Create a new task for the authenticated user.
    User ID in path must match authenticated user.
    """
    logger.info(f"Creating new task for user_id: {user_id}")
    logger.info(f"Incoming task data: {task}")
    logger.info(f"Task type: {type(task)}")
    logger.info(f"Task fields: title={getattr(task, 'title', 'NOT_FOUND')}, description={getattr(task, 'description', 'NOT_FOUND')}, completed={getattr(task, 'completed', 'NOT_FOUND')}")

    # Verify user_id matches authenticated user
    token_user_id = current_user.get("sub")
    path_user_id = str(user_id)
    logger.info(f"Create task - Token user_id: '{token_user_id}' (type: {type(token_user_id)})")
    logger.info(f"Create task - Path user_id: '{path_user_id}' (type: {type(path_user_id)})")

    if str(token_user_id) != str(path_user_id):
        logger.warning(f"Unauthorized attempt to create task for user {path_user_id} by user {token_user_id}")
        logger.warning(f"Mismatch: token_user_id='{token_user_id}' vs path_user_id='{path_user_id}'")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to create tasks for this user. Token user: {token_user_id}, Requested user: {path_user_id}"
        )

    # Set the user_id from the path parameter to ensure consistency
    logger.info(f"Creating task with user_id={user_id}, title='{task.title}', description='{task.description}', completed={task.completed}")

    # Convert request schema to model for database operation
    from ..models.task import TaskCreate as ModelTaskCreate
    task_with_user_id = ModelTaskCreate(
        user_id=user_id,
        title=task.title,
        description=task.description,
        completed=task.completed
    )

    db_task = create_task_for_user(task_with_user_id, db)
    logger.info(f"Successfully created task with id: {db_task.id} for user_id: {user_id}")
    return db_task


@router.get("/{user_id}/tasks/{id}", response_model=TaskRead)
def read_task(user_id: int, id: int, db: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    """
    Retrieve a specific task by ID for the authenticated user.
    User ID in path must match authenticated user.
    """
    logger.info(f"Fetching task {id} for user_id: {user_id}")

    # Verify user_id matches authenticated user
    token_user_id = current_user.get("sub")
    path_user_id = str(user_id)
    logger.info(f"Read task - Token user_id: '{token_user_id}' (type: {type(token_user_id)})")
    logger.info(f"Read task - Path user_id: '{path_user_id}' (type: {type(path_user_id)})")

    if str(token_user_id) != str(path_user_id):
        logger.warning(f"Unauthorized access attempt to task {id} by user {user_id}")
        logger.warning(f"Mismatch: token_user_id='{token_user_id}' vs path_user_id='{path_user_id}'")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to access this user's tasks. Token user: {token_user_id}, Requested user: {path_user_id}"
        )

    db_task = get_task_by_id_and_user(id, user_id, db)
    if not db_task:
        logger.info(f"Task {id} not found for user {user_id}")
        raise HTTPException(status_code=404, detail="Task not found")

    logger.info(f"Successfully retrieved task {id} for user {user_id}")
    return db_task


@router.put("/{user_id}/tasks/{id}", response_model=TaskRead)
def update_task(user_id: int, id: int, task_update: TaskUpdate, db: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    """
    Update a specific task by ID for the authenticated user.
    User ID in path must match authenticated user.
    """
    logger.info(f"Updating task {id} for user_id: {user_id}")

    # Verify user_id matches authenticated user
    token_user_id = current_user.get("sub")
    path_user_id = str(user_id)
    logger.info(f"Update task - Token user_id: '{token_user_id}' (type: {type(token_user_id)})")
    logger.info(f"Update task - Path user_id: '{path_user_id}' (type: {type(path_user_id)})")

    if str(token_user_id) != str(path_user_id):
        logger.warning(f"Unauthorized attempt to update task {id} by user {token_user_id}")
        logger.warning(f"Mismatch: token_user_id='{token_user_id}' vs path_user_id='{path_user_id}'")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to update this user's tasks. Token user: {token_user_id}, Requested user: {path_user_id}"
        )

    db_task = update_task_for_user(id, user_id, task_update, db)
    if not db_task:
        logger.info(f"Task {id} not found for user {user_id}")
        raise HTTPException(status_code=404, detail="Task not found")

    logger.info(f"Successfully updated task {id} for user {user_id}")
    return db_task


@router.delete("/{user_id}/tasks/{id}")
def delete_task(user_id: int, id: int, db: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    """
    Delete a specific task by ID for the authenticated user.
    User ID in path must match authenticated user.
    """
    logger.info(f"Deleting task {id} for user_id: {user_id}")

    # Verify user_id matches authenticated user
    token_user_id = current_user.get("sub")
    path_user_id = str(user_id)
    logger.info(f"Delete task - Token user_id: '{token_user_id}' (type: {type(token_user_id)})")
    logger.info(f"Delete task - Path user_id: '{path_user_id}' (type: {type(path_user_id)})")

    if str(token_user_id) != str(path_user_id):
        logger.warning(f"Unauthorized attempt to delete task {id} by user {token_user_id}")
        logger.warning(f"Mismatch: token_user_id='{token_user_id}' vs path_user_id='{path_user_id}'")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to delete this user's tasks. Token user: {token_user_id}, Requested user: {path_user_id}"
        )

    success = delete_task_for_user(id, user_id, db)
    if not success:
        logger.info(f"Task {id} not found for user {user_id}")
        raise HTTPException(status_code=404, detail="Task not found")

    logger.info(f"Successfully deleted task {id} for user {user_id}")
    return {"message": "Task deleted successfully"}


@router.patch("/{user_id}/tasks/{id}/complete", response_model=TaskRead)
def toggle_task_complete(user_id: int, id: int, task_toggle: TaskToggleComplete, db: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    """
    Toggle completion status of a specific task by ID for the authenticated user.
    User ID in path must match authenticated user.
    """
    logger.info(f"Toggling completion status for task {id} (completed: {task_toggle.completed}) for user_id: {user_id}")

    # Verify user_id matches authenticated user
    token_user_id = current_user.get("sub")
    path_user_id = str(user_id)
    logger.info(f"Update task - Token user_id: '{token_user_id}' (type: {type(token_user_id)})")
    logger.info(f"Update task - Path user_id: '{path_user_id}' (type: {type(path_user_id)})")

    if str(token_user_id) != str(path_user_id):
        logger.warning(f"Unauthorized attempt to update task {id} by user {token_user_id}")
        logger.warning(f"Mismatch: token_user_id='{token_user_id}' vs path_user_id='{path_user_id}'")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to update this user's tasks. Token user: {token_user_id}, Requested user: {path_user_id}"
        )

    db_task = toggle_task_completion(id, user_id, task_toggle, db)
    if not db_task:
        logger.info(f"Task {id} not found for user {user_id}")
        raise HTTPException(status_code=404, detail="Task not found")

    logger.info(f"Successfully toggled completion status for task {id} for user {user_id}")
    return db_task