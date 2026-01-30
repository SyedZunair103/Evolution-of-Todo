# Phase 2 Technical Implementation Plan: Full-Stack Web Application

## High-Level Architecture Update

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

## Tech Decisions & Justification

### 1. Next.js 16+ with App Router
- **Why**: Modern React framework with server components, improved performance, SEO
- **Benefits**: Built-in routing, server-side rendering, optimized bundling
- **Alternative**: Traditional pages router (older, less flexible)

### 2. shadcn/ui + Tailwind CSS
- **Why**: Pre-built accessible components with easy customization
- **Benefits**: Rapid development, consistent design, accessibility built-in
- **Alternative**: Custom components (time-consuming, potential accessibility issues)

### 3. FastAPI + SQLModel
- **Why**: High-performance ASGI framework with automatic API documentation
- **Benefits**: Type hints, automatic validation, async support, SQLModel ORM
- **Alternative**: Django (heavier, more complex for this use case)

### 4. Better Auth with JWKS Verification
- **Why**: Modern authentication solution with JWT support and JWKS for security
- **Benefits**: Easy setup, social login options, secure JWT handling
- **Security**: JWKS verification instead of shared secrets for asymmetric signing

### 5. Neon Serverless PostgreSQL
- **Why**: Serverless database with instant scaling and generous free tier
- **Benefits**: No infrastructure management, automatic backups, global distribution
- **Performance**: Low-latency connections with connection pooling

## Folder Structure Creation

```
evolution-of-todo/
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
│   │   ├── ui/               # shadcn/ui components
│   │   ├── auth/             # Authentication components
│   │   └── tasks/            # Task management components
│   ├── lib/                   # Utility functions
│   │   ├── auth.ts          # Auth utilities
│   │   └── api.ts           # API client utilities
│   ├── hooks/                 # Custom React hooks
│   │   └── useAuth.ts        # Authentication hook
│   ├── public/                # Static assets
│   ├── package.json
│   ├── tailwind.config.ts
│   ├── components.json
│   └── next.config.js
├── backend/                    # FastAPI application
│   ├── src/
│   │   ├── main.py            # FastAPI app entry point
│   │   ├── models/            # SQLModel models
│   │   │   ├── user.py       # User model
│   │   │   ├── task.py       # Task model
│   │   │   └── base.py       # Base model
│   │   ├── database/          # Database connection
│   │   │   ├── config.py     # Database config
│   │   │   └── session.py    # Database session
│   │   ├── auth/              # Authentication
│   │   │   ├── jwt.py        # JWT utilities
│   │   │   ├── deps.py       # Auth dependencies
│   │   │   └── jwks.py       # JWKS verification
│   │   ├── routers/           # API route handlers
│   │   │   ├── auth.py       # Auth routes
│   │   │   ├── tasks.py      # Task routes
│   │   │   └── users.py      # User routes
│   │   └── utils/             # Utility functions
│   ├── requirements.txt
│   └── alembic/               # Database migrations
├── docker-compose.yml         # Container orchestration
├── .env.example              # Environment variables template
├── README.md                 # Project documentation
└── CLAUDE.md                 # Claude Code history
```

## Step-by-Step Implementation Order

### Phase 1: Monorepo Setup
1. Create directory structure as outlined above
2. Initialize frontend with `npx create-next-app@latest`
3. Set up backend with FastAPI project structure
4. Create `.env.example` with all required environment variables
5. Configure `docker-compose.yml` for local development

### Phase 2: Backend Foundation
1. Implement SQLModel models (User, Task) with proper relationships
2. Set up database connection and session management
3. Create JWT utilities and JWKS verification dependency
4. Implement authentication middleware
5. Create base API structure with error handling

### Phase 3: API Endpoints
1. Build task CRUD endpoints with user_id filtering
2. Implement user isolation in all endpoints
3. Add proper request/response models
4. Create API documentation and validation
5. Implement pagination for task lists

### Phase 4: Frontend Authentication
1. Set up Better Auth in Next.js App Router
2. Create protected route components
3. Implement auth context and hooks
4. Build login/signup forms using shadcn/ui
5. Create middleware for route protection

### Phase 5: Task Management UI
1. Develop reusable task components (TaskList, TaskCard, TaskForm)
2. Create dashboard layout with navigation
3. Implement responsive design with Tailwind
4. Add loading states and error handling
5. Create confirmation dialogs for destructive actions

### Phase 6: API Integration
1. Implement API client with JWT interceptor
2. Connect frontend components to backend endpoints
3. Add real-time feedback for user actions
4. Implement optimistic updates where appropriate
5. Create error boundaries for API failures

### Phase 7: Security & Optimization
1. Configure CORS and security headers
2. Implement rate limiting
3. Add input sanitization
4. Optimize database queries
5. Set up production build configurations

## Environment Variables (.env.example)

```env
# Database
DATABASE_URL="postgresql://username:password@localhost:5432/todo_db"
NEON_DATABASE_URL="postgresql://username:password@ep-..."

# Authentication
BETTER_AUTH_URL="http://localhost:4000"
JWT_ISSUER="http://localhost:4000"
NEXT_PUBLIC_BETTER_AUTH_URL="http://localhost:4000"

# Next.js
NEXTAUTH_URL="http://localhost:3000"
NEXT_PUBLIC_APP_URL="http://localhost:3000"

# FastAPI
API_HOST="0.0.0.0"
API_PORT=8000
API_URL="http://localhost:8000"

# Security
BETTER_AUTH_SECRET="your-secret-key-here"
CORS_ORIGINS="http://localhost:3000,http://localhost:4000,https://your-app.vercel.app"

# Development
DEBUG=true
```

## Authentication Flow (JWKS-based)

### Frontend (Better Auth)
1. Initialize Better Auth client in Next.js
2. Create auth pages with login/signup forms
3. Store session tokens securely
4. Implement protected route wrapper

### Backend (JWKS Verification)
1. Create JWKS client to fetch public keys from Better Auth
2. Implement JWT dependency with signature verification
3. Extract user_id from verified tokens
4. Apply user_id filtering to all data access

### Security Measures
- Use asymmetric JWT signing (RS256)
- JWKS endpoint for key rotation support
- Short-lived access tokens
- Secure token storage and transmission

## Testing Plan

### Local Development Testing
1. Run backend: `uvicorn src.main:app --reload`
2. Run frontend: `npm run dev`
3. Test API endpoints with curl:
   ```bash
   # Login to get JWT
   curl -X POST http://localhost:4000/api/auth/signin -d '{"email":"user@example.com","password":"password"}'

   # Access protected endpoint
   curl -H "Authorization: Bearer <jwt_token>" http://localhost:8000/api/users/1/tasks
   ```

### Integration Testing
1. Test user registration and login flow
2. Verify task CRUD operations work with proper user isolation
3. Test JWT expiration and refresh
4. Validate error handling and security measures

## Vercel Deployment Steps

### Frontend Deployment
1. Connect Vercel to GitHub repository
2. Set build command: `npm run build`
3. Set output directory: `out`
4. Configure environment variables in Vercel dashboard
5. Set up custom domain (optional)

### Backend Deployment Options
1. **Railway**: Easy FastAPI deployment with PostgreSQL integration
2. **Render**: Python app hosting with free tier
3. **Self-hosted**: Docker container deployment
4. **AWS/GCP**: Cloud platform deployment

### Environment Configuration
- Set production DATABASE_URL to Neon production connection
- Configure BETTER_AUTH_URL to production domain
- Set NEXT_PUBLIC_APP_URL to live domain
- Update CORS origins for production

## Recommended Implementation Strategy

### Sprint 1: Foundation (Days 1-3)
1. Set up monorepo structure
2. Initialize Next.js app with shadcn/ui
3. Create FastAPI project structure
4. Implement basic models and database setup

### Sprint 2: Authentication (Days 4-6)
1. Integrate Better Auth with Next.js
2. Implement JWKS verification in FastAPI
3. Create protected routes and components
4. Test authentication flow

### Sprint 3: Core Features (Days 7-10)
1. Build task CRUD API endpoints
2. Create task management UI components
3. Connect frontend to backend API
4. Implement user isolation

### Sprint 4: Polish & Deploy (Days 11-14)
1. Add responsive design and accessibility
2. Implement error handling and loading states
3. Set up CI/CD pipeline
4. Deploy to production

This approach ensures a working baseline early while allowing for progressive enhancement based on testing and user feedback.