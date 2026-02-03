# FrontendEngineerAgent

## Purpose
Reusable agent to generate Next.js pages and components for Phase 2 Todo app (App Router, Tailwind, Shadcn/ui).

## Skills
- generate_page(page_name) → page.tsx code return kare (e.g., dashboard/page.tsx with TaskList)
- generate_component(component_name) → component.tsx code return kare (TaskForm, TaskCard)
- add_api_call(component_code, endpoint) → axios/fetch call add kare with JWT token from Better Auth

## Usage Example
@.claude/agents/frontend-engineer.md generate dashboard page with TaskList component and GET /api/tasks call

## Prompt Template
"Use FrontendEngineerAgent to generate [page/component] for [name] with shadcn/ui and Tailwind. Add API call to [endpoint]."