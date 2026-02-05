"""
Storage module for the Todo CLI Application.

This module implements in-memory storage for tasks with CRUD operations.
"""

from typing import Dict, List, Optional
from .models import Task


class InMemoryStore:
    """
    Manages collection of Task entities in memory with the following capabilities:
    - Tasks storage: Dictionary mapping ID (int) to Task objects
    - Auto-increment counter: Tracks next available ID
    - CRUD operations: Create, Read, Update, Delete functionality for tasks
    """

    def __init__(self):
        """Initialize the storage with an empty task dictionary and ID counter."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def _generate_next_id(self) -> int:
        """Generate and return the next available ID."""
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_task(self, title: str, description: str = "") -> int:
        """
        Creates new task, validates title, assigns auto-incremented ID.

        Args:
            title: The required title for the task
            description: The optional description for the task

        Returns:
            The ID of the newly created task

        Raises:
            ValueError: If the title is empty or invalid
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task_id = self._generate_next_id()
        task = Task(id=task_id, title=title.strip(), description=description.strip())
        self._tasks[task_id] = task
        return task_id

    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks sorted by ID.

        Returns:
            A list of all tasks sorted by ID
        """
        return sorted(self._tasks.values(), key=lambda x: x.id)

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieves specific task by ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, title: str, description: str) -> bool:
        """
        Updates task fields if exists.

        Args:
            task_id: The ID of the task to update
            title: The new title for the task
            description: The new description for the task

        Returns:
            True if the task was updated, False if the task doesn't exist
        """
        if task_id not in self._tasks:
            return False

        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task = self._tasks[task_id]
        task.title = title.strip()
        task.description = description.strip()
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Removes task if exists.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if the task doesn't exist
        """
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True

    def toggle_task_status(self, task_id: int) -> bool:
        """
        Flips completion status if exists.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if the task status was toggled, False if the task doesn't exist
        """
        if task_id not in self._tasks:
            return False

        task = self._tasks[task_id]
        task.completed = not task.completed
        return True