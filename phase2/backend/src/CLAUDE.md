# Backend Development Guidelines

## Tech Stack
- FastAPI for web framework
- SQLModel for ORM and database modeling
- Neon Serverless PostgreSQL for database
- Better Auth JWT validation for authentication
- Pydantic for data validation

## File Structure
- `api/` - API route handlers
- `models/` - SQLModel database models
- `auth/` - Authentication and authorization utilities
- `database/` - Database connection and session management
- `schemas/` - Pydantic schemas for request/response validation

## API Implementation
- Implement all 6 REST endpoints as specified
- Validate JWT tokens using BETTER_AUTH_SECRET
- Ensure user isolation by checking user_id in requests
- Implement proper error handling and status codes
- Use dependency injection for database sessions and authentication

## Authentication
- Validate JWT tokens from Authorization header
- Extract user_id from JWT payload
- Verify user_id in URL matches authenticated user
- Return 403 for unauthorized access attempts