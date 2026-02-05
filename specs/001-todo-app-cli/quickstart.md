# Quickstart Guide: Phase I Todo CLI Application

## Prerequisites

- Python 3.13+ installed on your system
- Basic familiarity with command-line interfaces

## Setup Instructions

1. **Clone or create the project structure**:
   ```
   src/
   ├── main.py       # Entry point and application runner
   ├── models.py     # Task dataclass definition
   ├── storage.py    # InMemoryStore class with CRUD operations
   └── cli.py        # CLI interface, menu loop, and user interaction handlers
   ```

2. **Navigate to the project root directory** where the src/ folder is located.

## Running the Application

1. From the project root directory, run:
   ```bash
   python src/main.py
   ```

2. The application will start with an interactive menu.

## Using the Application

Once the application starts, you'll see a menu with the following options:

```
Todo CLI Application
====================
1. Add task
2. View all tasks
3. Update task
4. Delete task
5. Toggle complete
0. Exit
Choose an option (0-5):
```

### Adding a Task
1. Select option 1
2. Enter the task title when prompted
3. Optionally enter a description (press Enter to skip)
4. The task will be added with an auto-incremented ID

### Viewing All Tasks
1. Select option 2
2. All tasks will be displayed in a formatted table with columns: ID | Title | Description | Status

### Updating a Task
1. Select option 3
2. Enter the task ID you want to update
3. Enter the new title
4. Optionally enter a new description (press Enter to keep current)
5. The task will be updated

### Deleting a Task
1. Select option 4
2. Enter the task ID you want to delete
3. The task will be removed from the list

### Toggling Task Completion
1. Select option 5
2. Enter the task ID you want to toggle
3. The completion status will flip (pending ↔ complete)

### Exiting the Application
1. Select option 0
2. The application will close

## Error Handling

The application will display clear error messages for:
- Invalid menu selections
- Non-existent task IDs
- Empty titles when adding/updating tasks
- Invalid numeric inputs

The application will not crash and will return to the main menu after displaying an error.