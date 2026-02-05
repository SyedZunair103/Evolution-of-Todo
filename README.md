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
├── frontend/               # Phase II: Next.js frontend application
├── backend/                # Phase II: FastAPI backend application
├── specs/                  # Specifications for each phase
│   ├── 001-todo-app-cli/   # Phase I specification
│   └── 002-web-app-fullstack/ # Phase II specification
├── history/                # Prompt history records
├── docker-compose.yml      # Docker configuration
├── .env.example           # Environment variables template
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

## Phase II: Full-Stack Web Application (In Progress)

**Status**: 🔄 In Progress

Full-stack web application with authentication:
- Frontend: Next.js 16+ (App Router)
- Backend: FastAPI + SQLModel
- Database: Neon Serverless PostgreSQL
- Auth: Better Auth + JWKS-based JWT verification
- User-isolated task management
- Responsive web UI implementation

**Technology Stack**:
- **Frontend**: Next.js 16+, React, TypeScript, Tailwind CSS, shadcn/ui
- **Backend**: FastAPI, SQLModel, Python
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWKS verification
- **Deployment**: Vercel (frontend), Railway/Render (backend)

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

### Phase I: CLI Todo Application

To run the Phase I Todo CLI Application:

1. Navigate to the phase1 directory:
   ```bash
   cd phase1
   ```

2. Run the application:
   ```bash
   python -m src.main
   ```

3. Run the tests:
   ```bash
   python test_app.py
   ```

### Phase II: Full-Stack Web Application

#### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the environment variables:
```bash
cp ../.env.example .env
```

5. Update the .env file with your configuration

6. Run the application:
```bash
uvicorn src.main:app --reload
```

#### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Copy the environment variables:
```bash
cp .env.example .env.local
```

4. Update the .env.local file with your configuration

5. Run the development server:
```bash
npm run dev
```

### Docker Setup

To run the entire application with Docker:

```bash
docker-compose up --build
```

## Features

### Phase 1 Features
- ✅ Add tasks with title and description
- ✅ View all tasks in a formatted table
- ✅ Update tasks by ID
- ✅ Delete tasks by ID
- ✅ Toggle task completion status
- ✅ Input validation and error handling
- ✅ Auto-incrementing task IDs

### Phase 2 Features
- ✅ User authentication and authorization
- ✅ User-isolated task management
- ✅ Persistent storage with PostgreSQL
- ⏳ Responsive web UI
- ⏳ JWT-based authentication
- ⏳ Advanced features (tags, search, priorities)

## Architecture

The full-stack application follows a microservice-like architecture:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Browser     │────▶│   Next.js App    │────▶│  FastAPI API    │────▶│ Neon PostgreSQL │
│ (Frontend)    │     │    (Next.js)     │     │   (FastAPI)     │     │   (Database)    │
│               │     │                  │     │                 │     │                 │
│ - React UI    │     │ - App Router     │     │ - JWT Auth      │     │ - User table    │
│ - Auth forms  │     │ - Protected routes│    │ - Task CRUD     │     │ - Task table    │
│ - Task views  │     │ - API calls      │     │ - User scoping  │     │ - Relations     │
└─────────────────┘     └──────────────────┘     └─────────────────┘     └─────────────────┘
                              │                           │
                              │      ┌─────────────┐      │
                              │─────▶│ Better Auth │◀─────│
                              │      │ (Identity)  │      │
                              │      └─────────────┘      │
                              │                           │
                              └───────────────────────────┘
                                    JWT Token Flow (JWKS)
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