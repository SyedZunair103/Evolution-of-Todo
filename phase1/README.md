# Todo CLI Application

A simple command-line interface application for managing todo tasks with in-memory storage.

## Features

- Add tasks with title and optional description
- View all tasks in a formatted table
- Update existing tasks
- Delete tasks
- Toggle task completion status
- Input validation and error handling

## Requirements

- Python 3.13+

## Setup

1. Clone or download the repository
2. Navigate to the project directory

## Usage

To run the application:

```bash
python -m src.main
```

Alternatively, if you're in the phase1 directory:

```bash
python -m src.main
```

## Functionality

The application provides the following options:

1. **Add task**: Create a new task with a required title and optional description
2. **View all tasks**: Display all tasks in a formatted table with ID, Title, Description, and Status
3. **Update task**: Modify an existing task's title or description by ID
4. **Delete task**: Remove a task by ID
5. **Toggle complete**: Flip the completion status of a task (pending ↔ complete) by ID
6. **Exit**: Close the application

## Task Status

- Pending tasks are marked with ☐
- Completed tasks are marked with ✓

## Error Handling

The application includes comprehensive error handling for:
- Invalid menu selections
- Non-existent task IDs
- Empty titles when adding/updating tasks
- Invalid numeric inputs

The application will display clear error messages and return to the main menu without crashing.

## Architecture

The application follows a clean architecture with separation of concerns:

- `src/models.py`: Defines the Task dataclass and validation functions
- `src/storage.py`: Implements the InMemoryStore class with CRUD operations
- `src/cli.py`: Contains the command-line interface functions
- `src/main.py`: Main application entry point with the menu loop