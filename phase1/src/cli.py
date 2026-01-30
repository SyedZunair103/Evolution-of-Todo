"""
CLI module for the Todo CLI Application.

This module implements the command-line interface for interacting with tasks.
"""

import sys
from typing import Optional
from .models import Task
from .storage import InMemoryStore


def display_menu():
    """Display the main menu options to the user."""
    print("\nTodo CLI Application")
    print("====================")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Toggle complete")
    print("0. Exit")
    print()


def get_user_choice() -> int:
    """
    Get and validate user menu choice.

    Returns:
        The user's menu choice as an integer
    """
    while True:
        try:
            choice = input("Choose an option (0-5): ").strip()
            choice_num = int(choice)
            if 0 <= choice_num <= 5:
                return choice_num
            else:
                print("Invalid choice. Please enter a number between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_task_input(is_update: bool = False) -> tuple[str, str]:
    """
    Get task details from user input.

    Args:
        is_update: Whether this is for an update operation (makes some fields optional)

    Returns:
        A tuple containing (title, description)
    """
    if is_update:
        print("Enter new details (leave blank to keep current value):")

    title = input("Enter task title: ").strip()

    if not is_update and not title:
        raise ValueError("Task title cannot be empty")

    description = input("Enter task description (optional): ").strip()

    return title, description


def get_task_id(prompt: str = "Enter task ID: ") -> int:
    """
    Get and validate task ID from user input.

    Args:
        prompt: The prompt to display to the user

    Returns:
        The validated task ID as an integer
    """
    while True:
        try:
            task_id_str = input(prompt).strip()
            task_id = int(task_id_str)
            if task_id > 0:
                return task_id
            else:
                print("Task ID must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def display_tasks(tasks: list[Task]):
    """
    Display all tasks in a formatted table.

    Args:
        tasks: List of tasks to display
    """
    if not tasks:
        print("No tasks found.")
        return

    print("\nTask List:")
    print(f"{'ID':<4} {'Title':<20} {'Description':<30} {'Status':<8}")
    print("-" * 66)

    for task in tasks:
        status = "✓" if task.completed else "☐"
        title = task.title[:18] + ".." if len(task.title) > 18 else task.title
        description = task.description[:28] + ".." if len(task.description) > 28 else task.description
        print(f"{task.id:<4} {title:<20} {description:<30} {status:<8}")


def display_add_task(store: InMemoryStore):
    """
    Handle the add task functionality.

    Args:
        store: The storage instance to use
    """
    try:
        title, description = get_task_input()
        task_id = store.add_task(title, description)
        print(f"Task added successfully with ID: {task_id}")

        # Show updated task list
        tasks = store.get_all_tasks()
        display_tasks(tasks)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred while adding task: {e}")


def display_view_tasks(store: InMemoryStore):
    """
    Handle the view all tasks functionality.

    Args:
        store: The storage instance to use
    """
    try:
        tasks = store.get_all_tasks()
        display_tasks(tasks)
    except Exception as e:
        print(f"An error occurred while viewing tasks: {e}")


def display_update_task(store: InMemoryStore):
    """
    Handle the update task functionality.

    Args:
        store: The storage instance to use
    """
    try:
        task_id = get_task_id("Enter task ID to update: ")

        # Check if task exists
        existing_task = store.get_task(task_id)
        if not existing_task:
            print(f"No task found with ID {task_id}.")
            return

        print(f"Current task: {existing_task.title}")
        title, description = get_task_input(is_update=True)

        # Use existing values if user input is empty
        if not title:
            title = existing_task.title
        if not description:
            description = existing_task.description

        success = store.update_task(task_id, title, description)
        if success:
            print(f"Task {task_id} updated successfully.")

            # Show updated task list
            tasks = store.get_all_tasks()
            display_tasks(tasks)
        else:
            print(f"Failed to update task {task_id}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred while updating task: {e}")


def display_delete_task(store: InMemoryStore):
    """
    Handle the delete task functionality.

    Args:
        store: The storage instance to use
    """
    try:
        task_id = get_task_id("Enter task ID to delete: ")

        # Check if task exists
        existing_task = store.get_task(task_id)
        if not existing_task:
            print(f"No task found with ID {task_id}.")
            return

        success = store.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully.")

            # Show updated task list
            tasks = store.get_all_tasks()
            display_tasks(tasks)
        else:
            print(f"Failed to delete task {task_id}.")
    except Exception as e:
        print(f"An error occurred while deleting task: {e}")


def display_toggle_task(store: InMemoryStore):
    """
    Handle the toggle task completion functionality.

    Args:
        store: The storage instance to use
    """
    try:
        task_id = get_task_id("Enter task ID to toggle: ")

        # Check if task exists
        existing_task = store.get_task(task_id)
        if not existing_task:
            print(f"No task found with ID {task_id}.")
            return

        success = store.toggle_task_status(task_id)
        if success:
            status = "completed" if existing_task.completed else "pending"
            print(f"Task {task_id} status toggled successfully. Now {status}.")

            # Show updated task list
            tasks = store.get_all_tasks()
            display_tasks(tasks)
        else:
            print(f"Failed to toggle task {task_id}.")
    except Exception as e:
        print(f"An error occurred while toggling task: {e}")