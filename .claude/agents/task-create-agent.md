# TaskCreateAgent

## Purpose
Reusable sub-agent for creating new tasks (POST /api/{user_id}/tasks).

## Skills
- create_task(title: str, description: str, user_id: int, db: Session) → Task model create kare, Neon DB save kare, return task dict
- validate_task_input(title, description) → Title required, length check

## Usage Example
@.claude/agents/task-create-agent.md create task with title "Buy groceries" and description "Milk and bread"

## Prompt Template
"Use TaskCreateAgent to create a new task with title [title] and description [desc] for user_id [user_id]."