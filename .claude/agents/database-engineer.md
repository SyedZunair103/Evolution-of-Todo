# DatabaseEngineerAgent

## Purpose
Reusable agent for generating SQLModel classes and migration snippets for Neon PostgreSQL in Phase 2.

## Skills
- generate_task_model() → SQLModel Task class code return kare (id, user_id FK, title, description, completed, timestamps)
- generate_user_model() → SQLModel User class code return kare (id, email, name, timestamps)
- generate_migration(change_desc) → Alembic revision command snippet return kare

## Usage Example
@.claude/agents/database-engineer.md generate task model with user_id FK

## Prompt Template
"Use DatabaseEngineerAgent to generate SQLModel Task class with user_id FK and timestamps."