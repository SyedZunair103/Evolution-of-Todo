# Monorepo Structure & Architecture

## Exact Folder Tree
```
evolution-of-todo/
├── .specify/                   # Spec-Kit configuration
├── specs/                      # All specifications
│   ├── 001-todo-app-cli/      # Phase I specification
│   └── 002-web-app-fullstack/ # Phase II specification
├── frontend/                   # Next.js application
│   ├── app/                    # App Router pages
│   │   ├── (auth)/            # Auth pages
│   │   │   ├── login/page.tsx
│   │   │   ├── signup/page.tsx
│   │   │   └── layout.tsx
│   │   ├── dashboard/         # Protected routes
│   │   │   ├── page.tsx
│   │   │   └── layout.tsx
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/            # Reusable UI components
│   ├── lib/                   # Utility functions
│   ├── hooks/                 # Custom React hooks
│   ├── public/                # Static assets
│   ├── package.json
│   └── next.config.js
├── backend/                    # FastAPI application
│   ├── src/
│   │   ├── main.py            # FastAPI app entry point
│   │   ├── models/            # SQLModel models
│   │   ├── routers/           # API route handlers
│   │   ├── auth/              # JWT authentication
│   │   └── database/          # Database connection
│   ├── requirements.txt
│   └── alembic/               # Database migrations
├── docker-compose.yml         # Container orchestration
├── .env.example              # Environment variables template
├── README.md                 # Project documentation
└── CLAUDE.md                 # Claude Code history
```

## Architecture Diagram
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
                                    JWT Token Flow
```

## Why Spec-Kit Monorepo Best for Claude Code
- Single authoritative source for all specifications
- Clear separation of concerns between frontend and backend
- Easy to generate code for specific components
- Consistent architecture across all layers
- Streamlined deployment and development workflows