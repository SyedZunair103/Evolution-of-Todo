---
id: 0002
title: Create spec for todo app
stage: spec
date: 2026-01-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-app-cli
branch: 001-todo-app-cli
user: unknown
command: /sp.specify
labels: ["specification", "todo-app", "cli", "python"]
links:
  spec: specs/001-todo-app-cli/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - "specs/001-todo-app-cli/spec.md"
 - "specs/001-todo-app-cli/checklists/requirements.md"
tests:
 - none
---

## Prompt

# Phase I Spec – In-Memory Python Console Todo App
Project: Evolution of Todo – Phase I
Version: 1.0
Follows: 000-constitution.md (strictly – no manual code!)

## Goal
Build interactive CLI Todo app storing tasks **in memory only** (no files/DB).
Implement **only** the 5 basic features:
1. Add task (title required, description optional)
2. View all tasks (nice table: ID | Title | Desc | Status ✓/☐)
3. Update task (title/desc by ID)
4. Delete task (by ID)
5. Toggle complete (by ID)

## Constraints
- Python 3.13+, uv, stdlib only (no external deps)
- Clean code: type hints, docstrings, PEP 8, error handling
- Separation: models.py, storage.py, cli.py, main.py
- Interactive menu loop until exit (0)
- Validate inputs: non-empty title, valid int ID
- Auto-increment ID from 1
- After action → show updated list

## Structure (exact)
src/
├── main.py       # start CLI
├── models.py     # Task class/dataclass
├── storage.py    # InMemoryStore class
└── cli.py        # menu + handlers
text## Success Tests
- Add → shows in list, pending
- Toggle → flips ✓/☐
- Update/Delete → reflects correctly
- Invalid ID/empty title → clear error, no crash

## Claude Action
1. Confirm constitution + this spec compliance.
2. Generate full initial code for all src/ files + README.md setup instructions.
3. If long → step-by-step (models → storage → cli → main).

## Response snapshot

Created a comprehensive feature specification for the Phase I Todo CLI Application, defining user scenarios, functional requirements, and success criteria based on the provided feature description.

## Outcome

- ✅ Impact: Created detailed specification for todo CLI app with clear requirements
- 🧪 Tests: none
- 📁 Files: specs/001-todo-app-cli/spec.md, specs/001-todo-app-cli/checklists/requirements.md
- 🔁 Next prompts: /sp.plan to generate implementation plan
- 🧠 Reflection: Specification follows constitution requirements with clear user stories and testable acceptance criteria

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): Original specification creation
- Next experiment (smallest change to try): Proceed with planning phase to implement the specification