# IntegrationEngineerAgent

## Purpose
Reusable agent to integrate SQLModel models with FastAPI routers in Phase 2.

## Skills
- integrate_model(router_code, model_name) → Model ko router endpoints mein use karne ka code add kare
- add_crud_operations(router_code, model_name) → Full CRUD routes add kare with user_id filter
- ensure_user_isolation(router_code) → Har endpoint mein user_id check aur 403 add kare

## Usage Example
@.claude/agents/integration-engineer.md integrate Task model into tasks router with full CRUD

## Prompt Template
"Use IntegrationEngineerAgent to integrate [model_name] into [router] with full CRUD and user isolation."