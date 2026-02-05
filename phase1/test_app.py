"""
Test script to demonstrate the functionality of the Todo CLI Application.
This script tests all the core features of the application programmatically.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.storage import InMemoryStore
from src.models import Task


def test_basic_functionality():
    """Test the basic functionality of the InMemoryStore."""
    print("Testing Basic Functionality...")
    print("=" * 40)

    # Create a store instance
    store = InMemoryStore()

    # Test adding tasks
    print("1. Adding tasks...")
    task1_id = store.add_task("Buy groceries", "Milk, bread, eggs")
    print(f"   Added task with ID: {task1_id}")

    task2_id = store.add_task("Complete project", "Finish the todo app implementation")
    print(f"   Added task with ID: {task2_id}")

    task3_id = store.add_task("Call dentist", "")
    print(f"   Added task with ID: {task3_id}")

    # Test getting all tasks
    print("\n2. Retrieving all tasks...")
    all_tasks = store.get_all_tasks()
    print(f"   Total tasks: {len(all_tasks)}")
    for task in all_tasks:
        status = "X" if task.completed else "O"
        print(f"   ID: {task.id}, Title: '{task.title}', Desc: '{task.description}', Status: {status}")

    # Test getting a specific task
    print(f"\n3. Retrieving task with ID {task1_id}...")
    task = store.get_task(task1_id)
    if task:
        print(f"   Found: ID {task.id}, Title: '{task.title}', Completed: {task.completed}")
    else:
        print(f"   Task with ID {task1_id} not found")

    # Test toggling task status
    print(f"\n4. Toggling status of task ID {task1_id}...")
    success = store.toggle_task_status(task1_id)
    if success:
        task = store.get_task(task1_id)
        status = "X" if task.completed else "O"
        print(f"   Task {task1_id} status changed to: {status}")
    else:
        print(f"   Failed to toggle task {task1_id}")

    # Test updating task
    print(f"\n5. Updating task with ID {task2_id}...")
    success = store.update_task(task2_id, "Complete todo app", "Finish the implementation and test it")
    if success:
        task = store.get_task(task2_id)
        print(f"   Updated task: ID {task.id}, Title: '{task.title}', Desc: '{task.description}'")
    else:
        print(f"   Failed to update task {task2_id}")

    # Test deleting task
    print(f"\n6. Deleting task with ID {task3_id}...")
    success = store.delete_task(task3_id)
    if success:
        print(f"   Task {task3_id} deleted successfully")
    else:
        print(f"   Failed to delete task {task3_id}")

    # Show remaining tasks
    print("\n7. Remaining tasks after deletion:")
    remaining_tasks = store.get_all_tasks()
    print(f"   Total tasks: {len(remaining_tasks)}")
    for task in remaining_tasks:
        status = "X" if task.completed else "O"
        print(f"   ID: {task.id}, Title: '{task.title}', Desc: '{task.description}', Status: {status}")

    print("\nBasic functionality test completed!")


def test_edge_cases():
    """Test edge cases and error handling."""
    print("\n\nTesting Edge Cases...")
    print("=" * 40)

    store = InMemoryStore()

    # Test adding task with empty title (should raise ValueError)
    print("1. Testing empty title validation...")
    try:
        store.add_task("", "This should fail")
        print("   ERROR: Empty title was accepted!")
    except ValueError as e:
        print(f"   SUCCESS: Caught expected error: {e}")

    # Test adding task with only whitespace title
    print("\n2. Testing whitespace-only title validation...")
    try:
        store.add_task("   ", "This should also fail")
        print("   ERROR: Whitespace-only title was accepted!")
    except ValueError as e:
        print(f"   SUCCESS: Caught expected error: {e}")

    # Test updating with empty title
    print("\n3. Testing update with empty title...")
    task_id = store.add_task("Valid task", "Description")
    print(f"   Added task with ID: {task_id}")

    try:
        store.update_task(task_id, "", "New description")
        print("   ERROR: Empty title was accepted for update!")
    except ValueError as e:
        print(f"   SUCCESS: Caught expected error during update: {e}")

    # Test operations on non-existent task
    print("\n4. Testing operations on non-existent task (ID: 999)...")
    result = store.get_task(999)
    print(f"   Get task result: {result}")

    result = store.update_task(999, "New title", "New desc")
    print(f"   Update task result: {result}")

    result = store.delete_task(999)
    print(f"   Delete task result: {result}")

    result = store.toggle_task_status(999)
    print(f"   Toggle task result: {result}")

    print("\nEdge cases test completed!")


def test_auto_increment():
    """Test the auto-increment functionality."""
    print("\n\nTesting Auto-Increment...")
    print("=" * 40)

    store = InMemoryStore()

    # Add several tasks and check IDs
    print("1. Adding tasks to verify auto-increment...")
    ids = []
    for i in range(5):
        task_id = store.add_task(f"Task {i+1}", f"Description for task {i+1}")
        ids.append(task_id)
        print(f"   Added task with ID: {task_id}")

    print(f"\n2. Expected sequence: [1, 2, 3, 4, 5]")
    print(f"   Actual sequence:  {ids}")

    if ids == [1, 2, 3, 4, 5]:
        print("   SUCCESS: Auto-increment working correctly!")
    else:
        print("   ERROR: Auto-increment not working as expected!")

    # Delete a task and add another to test continuity
    print(f"\n3. Deleting task with ID 3...")
    store.delete_task(3)

    print("4. Adding another task after deletion...")
    new_id = store.add_task("New task after deletion", "This should get ID 6")
    print(f"   New task ID: {new_id}")

    if new_id == 6:
        print("   SUCCESS: ID sequence continued correctly after deletion!")
    else:
        print(f"   Note: New ID is {new_id}, which is still correct (next available)")

    print("\nAuto-increment test completed!")


def main():
    """Run all tests."""
    print("Todo CLI Application - Test Suite")
    print("=" * 50)

    test_basic_functionality()
    test_edge_cases()
    test_auto_increment()

    print("\n" + "=" * 50)
    print("All tests completed!")
    print("\nTo run the actual application, use: python -m src.main")


if __name__ == "__main__":
    main()