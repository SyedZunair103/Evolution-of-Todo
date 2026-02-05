# Phase I: Todo CLI Application

This is the first phase of the "Evolution of Todo" project, implementing a console-based todo application with in-memory storage.

## Overview

The Todo CLI Application is a Python-based command-line interface application that allows users to manage their tasks through 5 core operations:
1. Add tasks (with required title and optional description)
2. View all tasks (displayed in a formatted table)
3. Update tasks (modify title/description by ID)
4. Delete tasks (remove by ID)
5. Toggle completion status (flip between pending ✓/☐ by ID)

## Architecture

The application follows a clean, modular architecture with clear separation of concerns:

### File Structure
```
src/
├── models.py     # Task dataclass definition
├── storage.py    # InMemoryStore class with CRUD operations
├── cli.py        # CLI interface, menu loop, and user interaction handlers
└── main.py       # Entry point and application runner
```

### Components

- **models.py**: Defines the `Task` dataclass with ID, Title, Description, and Completed status attributes
- **storage.py**: Implements the `InMemoryStore` class with methods for all CRUD operations
- **cli.py**: Contains all user interface functions including menu display, input handling, and formatted output
- **main.py**: Main application loop that orchestrates the CLI interface

## Features Implemented

✅ **Add Task**: Create new tasks with required title and optional description
✅ **View Tasks**: Display all tasks in a formatted table (ID | Title | Description | Status)
✅ **Update Task**: Modify existing tasks by ID
✅ **Delete Task**: Remove tasks by ID
✅ **Toggle Complete**: Flip completion status by ID
✅ **Input Validation**: Validate titles, IDs, and handle invalid inputs gracefully
✅ **Error Handling**: Comprehensive error handling without application crashes
✅ **Auto-increment IDs**: Automatic ID assignment starting from 1
✅ **Persistent Session**: Tasks persist during the application session (in-memory)

## Requirements

- Python 3.13+
- Standard library only (no external dependencies)

## Setup and Usage

1. Navigate to the `phase1` directory
2. Run the application:
   ```bash
   python -m src.main
   ```

   Alternatively:
   ```bash
   cd phase1
   python -m src.main
   ```

3. Use the interactive menu to perform operations:
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

## Design Decisions

- **In-Memory Storage**: Tasks are stored in a dictionary with integer keys for O(1) access
- **Auto-Increment IDs**: Sequential ID assignment starting from 1 using a counter
- **Clean Architecture**: Separation of concerns with distinct modules for data, storage, and UI
- **Input Validation**: Comprehensive validation for all user inputs
- **Error Handling**: Graceful error handling with user-friendly messages
- **Formatted Output**: Tabular display of tasks with proper alignment

## Code Quality

- **Type Hints**: Full type annotation coverage
- **Docstrings**: Comprehensive documentation for all functions, classes, and modules
- **PEP 8 Compliant**: Follows Python style guidelines
- **Modular Design**: Well-separated concerns across different modules

## Status

Phase I is complete with all 5 core features implemented and fully functional. The application is ready for use and demonstrates the foundation for the evolution of the todo application.