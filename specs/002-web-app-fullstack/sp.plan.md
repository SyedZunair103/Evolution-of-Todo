# Phase 2: Todo Full-Stack Web Application Implementation Plan

## Technical Context

### High-Level Architecture
```
┌─────────────────┐    HTTP/HTTPS    ┌─────────────────┐
│   Browser     │◄──────────────────►│   Next.js App   │
│ (Frontend)    │                   │   (Next.js)     │
│               │    API Calls      │                 │
└─────────────────┘◄──────────────────►│                 │
       │                              │                 │
       │ JWT Token                    │                 │
       └─────────────────────────────►│                 │
                                      │                 │
                                      │                 │
                                      │    ┌─────────────▼──────────┐
                                      │    │     FastAPI Backend    │
                                      │    │      (Python)          │
                                      │    └────────────────────────┘
                                      │              │
                                      │              │ Database Calls
                                      │              │
                                      │    ┌─────────▼─────────┐
                                      │    │ Neon PostgreSQL   │
                                      │    │   Database        │
                                      │    └───────────────────┘
                                      │
                                      └─────────────────────────┘
```

### Tech Decisions & Why
- **Shared JWT Secret**: Using BETTER_AUTH_SECRET for both frontend (Better Auth) and backend (JWT validation) ensures consistent authentication across the application
- **Tailwind CSS**: Chosen for rapid styling without the overhead of additional component libraries
- **Next.js App Router**: Provides server-side rendering capabilities and better performance
- **FastAPI**: Offers automatic API documentation, type validation, and high performance
- **SQLModel**: Combines SQLAlchemy and Pydantic for type-safe database models
- **Neon Serverless PostgreSQL**: Provides scalable, serverless database with automatic scaling

### Current Unknowns
- Specific database connection string for Neon
- BETTER_AUTH_SECRET value for JWT validation
- CORS configuration details for the specific domain

## Constitution Check

Based on the project constitution, this plan adheres to:
- Clean architecture principles with separation of concerns
- Type safety through SQLModel and Pydantic
- Security-first approach with JWT authentication
- Scalable infrastructure with serverless database

## Gates Evaluation

✅ All architectural decisions align with project principles
✅ No constitutional violations identified
✅ Security considerations properly addressed

## Phase 0: Research & Resolution of Unknowns

### Research Tasks

#### Task 1: Neon Database Configuration
**Research**: Determine proper connection string format for Neon Serverless PostgreSQL
**Rationale**: Essential for backend database connectivity
**Expected Outcome**: DATABASE_URL format for Neon

#### Task 2: BETTER_AUTH_SECRET Generation
**Research**: Best practices for generating secure JWT secrets
**Rationale**: Critical for authentication security
**Expected Outcome**: Recommended secret generation approach

#### Task 3: CORS Configuration
**Research**: Proper CORS setup for Next.js + FastAPI integration
**Rationale**: Required for frontend-backend communication
**Expected Outcome**: CORS middleware configuration

## Phase 1: Design & Contracts

### Step-by-Step Implementation Order

#### Step 1: Environment Setup (Parallel Tasks)
**Frontend & Backend**:
1. Create .env files with required environment variables
2. Set up project structure with Next.js and FastAPI
3. Install dependencies for both applications

**Required Environment Variables**:
- `DATABASE_URL` - Neon PostgreSQL connection string
- `BETTER_AUTH_SECRET` - Shared JWT secret for auth consistency
- `NEXT_PUBLIC_BETTER_AUTH_URL` - Frontend auth URL

#### Step 2: Database Layer Implementation
1. Create SQLModel User and Task models based on schema.md
2. Set up database connection and session management
3. Implement database initialization and migration scripts

#### Step 3: Backend API Implementation
1. Implement JWT validation middleware using BETTER_AUTH_SECRET
2. Create 6 required API endpoints:
   - GET /api/{user_id}/tasks
   - POST /api/{user_id}/tasks
   - GET /api/{user_id}/tasks/{id}
   - PUT /api/{user_id}/tasks/{id}
   - DELETE /api/{user_id}/tasks/{id}
   - PATCH /api/{user_id}/tasks/{id}/complete
3. Implement user isolation checks in all endpoints
4. Add proper error handling and validation

#### Step 4: Authentication Setup
1. Configure Better Auth in frontend with shared secret
2. Implement JWT token handling for API calls
3. Set up protected routes in Next.js
4. Create login/signup pages

#### Step 5: Frontend Implementation
1. Create UI components as specified in components.md
2. Implement pages as specified in pages.md
3. Connect frontend to backend API endpoints
4. Implement real-time updates and loading states

#### Step 6: Integration & Testing
1. Connect all components and verify functionality
2. Test user isolation (ensure users can't access others' data)
3. Verify JWT authentication flow
4. Test all 5 core features

### Dependencies & Setup

#### Backend Dependencies
- FastAPI
- SQLModel
- uvicorn
- python-multipart
- better-exceptions
- python-jose[cryptography]

#### Frontend Dependencies
- Next.js 16+
- React
- Tailwind CSS
- Better Auth
- axios or fetch for API calls

#### CORS Setup
- Configure backend to allow frontend domain
- Enable credentials for JWT cookie handling
- Allow necessary headers and methods

### Testing Plan

#### Local Development Testing
1. **API Testing**: Use curl or Postman to test all 6 endpoints
2. **Authentication Testing**: Verify JWT token generation and validation
3. **User Isolation Testing**: Create multiple users and verify data separation
4. **Frontend Testing**: Manual testing of all UI components and flows

#### Specific Tests
- Create tasks for User A, verify User B cannot access them
- Test all CRUD operations with proper authentication
- Verify JWT token validation in backend
- Test error handling for invalid requests

### Deployment Steps

#### Vercel Deployment (Frontend)
1. Configure Vercel to deploy from `frontend/` directory
2. Set environment variables in Vercel dashboard
3. Verify production build works correctly
4. Test deployed application functionality

#### Backend Deployment (Railway/Render)
1. Containerize FastAPI application
2. Set up production database connection
3. Configure environment variables
4. Deploy and verify API endpoints

### Risks & Mitigations

#### Risk 1: JWT Secret Mismatch
**Impact**: Authentication failures between frontend and backend
**Mitigation**:
- Use same BETTER_AUTH_SECRET in both environments
- Implement proper error logging for authentication failures
- Verify secret format and encoding

#### Risk 2: Neon Connection Issues
**Impact**: Database connectivity problems in production
**Mitigation**:
- Implement connection pooling and retry logic
- Monitor connection health
- Set up proper connection string validation

#### Risk 3: User Data Isolation Failure
**Impact**: Users accessing other users' tasks
**Mitigation**:
- Implement strict user_id validation in all endpoints
- Add comprehensive testing for data isolation
- Use database-level constraints where possible

#### Risk 4: CORS Configuration Problems
**Impact**: Frontend unable to communicate with backend
**Mitigation**:
- Test CORS configuration locally before deployment
- Implement proper error handling for network requests
- Use environment-specific CORS settings

## Success Criteria

- All 5 core features implemented and working
- User authentication and isolation functioning properly
- API endpoints accessible and returning correct data
- Frontend UI responsive and user-friendly
- Production deployment successful on Vercel
- No security vulnerabilities in authentication system