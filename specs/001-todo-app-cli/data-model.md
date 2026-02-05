# Data Model: Phase I Todo CLI Application

## Entity: Task

**Definition**: Represents a single todo item with the following attributes:
- **ID** (int): Unique identifier, auto-incremented starting from 1
- **Title** (str): Required string representing the task name
- **Description** (str): Optional string with additional task details (can be empty)
- **Completed** (bool): Boolean indicating completion status (False=pending ☐, True=complete ✓)

**Validation Rules**:
- Title must not be empty when creating/updating
- ID must be a positive integer
- Description can be empty but not None

**State Transitions**:
- Pending (☐) → Complete (✓): When toggle operation is called on an incomplete task
- Complete (✓) → Pending (☐): When toggle operation is called on a completed task

## Entity: InMemoryStore

**Definition**: Manages collection of Task entities in memory with the following capabilities:
- **Tasks storage**: Dictionary mapping ID (int) to Task objects
- **Auto-increment counter**: Tracks next available ID
- **CRUD operations**: Create, Read, Update, Delete functionality for tasks

**Methods**:
- **add_task(title: str, description: str = "")** → int: Creates new task, validates title, assigns auto-incremented ID
- **get_all_tasks()** → List[Task]: Returns all tasks sorted by ID
- **get_task(task_id: int)** → Task or None: Retrieves specific task by ID
- **update_task(task_id: int, title: str, description: str)** → bool: Updates task fields if exists
- **delete_task(task_id: int)** → bool: Removes task if exists
- **toggle_task_status(task_id: int)** → bool: Flips completion status if exists

**Constraints**:
- All operations must validate existence before modifying
- Must handle invalid IDs gracefully
- Storage exists only in memory (transient)