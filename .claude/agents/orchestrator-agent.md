# OrchestratorAgent

## Purpose
Main reusable agent to coordinate all other agents for Phase 2 CRUD operations.

## Skills
- process_crud_request(action: str, data: dict, db: Session) → Request ko analyze kare, sahi agent ko call kare (create, list, update, delete, toggle)
- aggregate_results(sub_results) → Multiple agents ke results combine kare

## Usage Example
@.claude/agents/orchestrator-agent.md process "create_task" with data {"title": "Meeting", "description": "2 PM"}

## Prompt Template
"Use OrchestratorAgent to process [action] with data [data] for current user."