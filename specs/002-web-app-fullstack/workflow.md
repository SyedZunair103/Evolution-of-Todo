# Setup, Workflow & Claude Code Instructions

## Monorepo Initialization Steps
1. Create project structure following the exact tree above
2. Initialize Git repository with proper .gitignore
3. Set up .specify/ directory with Spec-Kit configuration
4. Create initial constitution.md based on hackathon requirements

## Development Workflow
1. Update constitution.md with any new requirements
2. Create feature specifications in specs/002-web-app-fullstack/
3. Generate implementation plan using Claude Code
4. Break plan into tasks and implement iteratively
5. Test each feature incrementally
6. Document changes in CLAUDE.md

## Claude Code Instructions
- Always generate code based on the latest specifications
- Follow the exact folder structure specified
- Maintain consistent naming conventions
- Include comprehensive error handling
- Add proper type annotations and documentation
- Implement security best practices by default

## CLAUDE.md Snippets
- Frontend: "Generate Next.js 16+ App Router components with TypeScript and shadcn/ui"
- Backend: "Generate FastAPI with SQLModel and JWT authentication using JWKS verification"
- Auth: "Implement Better Auth with JWKS-based token verification for Next.js/FastAPI"
- Database: "Create SQLModel models with proper relationships and indexes"

## Alembic Migration Instructions
- Initialize Alembic in backend/ directory
- Generate migration files after model changes
- Apply migrations before running the application
- Keep migration files in version control