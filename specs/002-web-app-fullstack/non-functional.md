# Non-Functional Requirements

## CORS Configuration
- Allow origin: Vercel deployment URL and localhost:3000
- Allow credentials: True for auth cookies
- Allow methods: GET, POST, PUT, PATCH, DELETE
- Allow headers: Content-Type, Authorization, X-Requested-With

## Environment Variables (.env.example)
```env
# Database
DATABASE_URL="postgresql://user:password@localhost:5432/todo_db"

# Authentication
BETTER_AUTH_URL="http://localhost:4000"
JWT_ISSUER="http://localhost:4000"

# Next.js
NEXT_PUBLIC_BETTER_AUTH_URL="http://localhost:4000"
NEXTAUTH_URL="http://localhost:3000"
```

## Performance Targets
- API response time: <200ms for simple operations
- Page load time: <1000ms for dashboard
- Database query time: <100ms for filtered queries
- Concurrent users: Support 100+ simultaneous users

## Security Requirements
- Never log JWT tokens or sensitive authentication data
- Use HTTPS in production environments
- Implement CSRF protection for form submissions
- Sanitize all user inputs before database operations
- Use parameterized queries to prevent SQL injection
- Verify JWT signatures using JWKS endpoint
- Validate user_id in JWT matches the requested resource