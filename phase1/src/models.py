"""
Models for the Todo CLI Application.

This module defines the data structures used in the application.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item with the following attributes:

    Attributes:
        id (int): Unique identifier, auto-incremented starting from 1
        title (str): Required string representing the task name
        description (str): Optional string with additional task details (can be empty)
        completed (bool): Boolean indicating completion status (False=pending ☐, True=complete ✓)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False


def validate_task_title(title: str) -> bool:
    """
    Validates that a task title is not empty.

    Args:
        title: The title to validate

    Returns:
        True if the title is valid (non-empty), False otherwise
    """
    return bool(title and title.strip())