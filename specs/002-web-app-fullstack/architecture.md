# Todo Full-Stack Web Application - Architecture

## Monorepo Structure
```
project-root/
├── .spec-kit/
│   └── config.yaml
├── specs/
│   ├── overview.md
│   ├── architecture.md
│   ├── features/task-crud.md
│   ├── authentication.md
│   ├── api/rest-endpoints.md
│   ├── database/schema.md
│   ├── ui/components.md
│   └── ui/pages.md
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── styles/
│   └── CLAUDE.md
├── backend/
│   ├── api/
│   ├── models/
│   ├── auth/
│   ├── database/
│   └── CLAUDE.md
├── docker-compose.yml
└── README.md
```

## System Architecture Diagram
```
┌─────────────────┐    HTTP/HTTPS    ┌─────────────────┐
│   Frontend      │◄────────────────►│   Backend       │
│ (Next.js 16+)   │                 │  (FastAPI)      │
│                 │    API Calls     │                 │
└─────────────────┘◄────────────────►│                 │
       │                              │                 │
       │ JWT Token                    │                 │
       └─────────────────────────────►│                 │
                                      │                 │
                                      │                 │
                                      │    ┌─────────────▼──────────┐
                                      │    │     Neon PostgreSQL    │
                                      │    │      Database          │
                                      │    └────────────────────────┘
                                      │             ▲
                                      └─────────────┼─────────────────┘
                                                    │
                                        SQL Queries │
                                                    │
                                                    └─────────────────┘
```

## Tech Stack
- **Frontend**: Next.js 16+ with App Router
- **Styling**: Tailwind CSS + Shadcn/ui components
- **Backend**: FastAPI with Python 3.10+
- **ORM/Database**: SQLModel with Neon Serverless PostgreSQL
- **Authentication**: Better Auth for frontend, JWT for backend
- **Deployment**: Docker containers with docker-compose
- **Environment**: Shared BETTER_AUTH_SECRET for JWT validation