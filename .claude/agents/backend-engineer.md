# BackendEngineerAgent

## Purpose
Reusable agent to generate FastAPI routers and endpoints for Phase 2 tasks.

## Skills
- generate_tasks_router() → APIRouter code return kare for /api/{user_id}/tasks with 5 endpoints
- add_endpoint(router_code, method, path) → new endpoint add kare with Depends(get_db, get_current_user)

## Usage Example
@.claude/agents/backend-engineer.md generate tasks router with GET / and POST / endpoints

## Prompt Template
"Use BackendEngineerAgent to generate FastAPI router for tasks with [method] [path]. Use Depends for auth and DB."