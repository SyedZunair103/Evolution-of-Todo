# The Evolution of Todo

This project demonstrates the evolution of a simple todo application through multiple phases, showcasing different architectures, technologies, and deployment strategies.

## Project Structure

```
evolution-of-todo/
├── phase1/                 # Phase I: In-memory Python Console App
│   ├── src/
│   │   ├── models.py       # Task dataclass definition
│   │   ├── storage.py      # InMemoryStore class with CRUD operations
│   │   ├── cli.py          # CLI interface, menu loop, and user interaction handlers
│   │   └── main.py         # Entry point and application runner
│   └── README.md           # Phase I documentation
├── specs/                  # Specifications for each phase
│   ├── 001-todo-app-cli/   # Phase I specification
│   └── 002-web-app-fullstack/ # Phase II specification (future)
├── history/                # Prompt history records
└── README.md               # This file
```

## Phase I: Todo CLI Application (Completed)

**Status**: ✅ Complete

A console-based todo application with in-memory storage, implementing the 5 core features:
1. Add task (title required, description optional)
2. View all tasks (formatted table: ID | Title | Desc | Status ✓/☐)
3. Update task (title/desc by ID)
4. Delete task (by ID)
5. Toggle complete (by ID)

**Technology Stack**:
- Python 3.13+
- Standard library only (no external dependencies)

**Features**:
- Clean, modular architecture with separation of concerns
- Input validation and comprehensive error handling
- Auto-incrementing task IDs
- Formatted table display
- Interactive menu system

## Phase II: Full-Stack Web Application (Planned)

**Status**: 🔄 Planned

Full-stack web application with authentication:
- Frontend: Next.js 16+ (App Router)
- Backend: FastAPI + SQLModel
- Database: Neon Serverless PostgreSQL
- Auth: Better Auth + JWT tokens

## Phase III: AI-Powered Chatbot (Planned)

**Status**: 🔄 Planned

AI-powered conversational chatbot using:
- OpenAI Agents SDK
- ChatKit
- Official MCP SDK

## Phase IV: Kubernetes Deployment (Planned)

**Status**: 🔄 Planned

Local Kubernetes deployment with:
- Docker containers
- Minikube
- Helm charts
- AIOps tools

## Phase V: Cloud-Native Architecture (Planned)

**Status**: 🔄 Planned

Advanced cloud-native implementation with:
- Kafka for event streaming
- Dapr for distributed application runtime
- DigitalOcean Kubernetes (DOKS)
- Event-driven architecture

## Getting Started

To run the Phase I Todo CLI Application:

1. Navigate to the phase1 directory:
   ```bash
   cd phase1
   ```

2. Run the application:
   ```bash
   python -m src.main
   ```

## Project Principles

This project follows the principles of Spec-Driven Development (SDD):
- Strict spec-driven development only
- No manual code editing
- Iterative spec refinement process
- Clean code and architecture principles
- Comprehensive documentation

## License

This project is part of the "Evolution of Todo" series demonstrating software architecture evolution.