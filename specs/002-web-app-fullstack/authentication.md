# Authentication System

## Better Auth + JWT Flow
The application implements a dual-layer authentication system using Better Auth for frontend authentication and JWT tokens for backend API communication.

### Frontend Authentication (Better Auth)
- Better Auth handles user registration, login, and session management on the frontend
- Provides social login capabilities (Google, GitHub, etc.) out of the box
- Manages user sessions and provides user identity information to the frontend
- Handles password reset and account recovery flows

### Backend Authentication (JWT)
- Frontend sends JWT tokens in Authorization header for all API requests
- Backend validates JWT tokens using the shared BETTER_AUTH_SECRET
- Token contains user identity information for authorization decisions
- Tokens expire after configured duration (default 7 days)

### Shared Secret Configuration
- BETTER_AUTH_SECRET environment variable must be identical in both frontend and backend
- Used to sign and verify JWT tokens for consistency between frontend and backend
- Should be a strong, randomly generated string of at least 32 characters
- Stored securely in environment variables, never committed to version control

### Security Benefits
- Strong protection against session hijacking
- Stateless authentication suitable for horizontal scaling
- Automatic token expiration reduces risk of long-lived compromised tokens
- Isolated user data access through user_id validation in all requests
- Prevention of cross-user data access through proper authorization checks