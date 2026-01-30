# Authentication & JWT Flow (Detailed)

## Better Auth Setup in Next.js
- Install `@better-auth/react` and `@better-auth/next-js`
- Configure `/app/api/auth/[...all]/route.ts` for API routes
- Initialize auth client in layout or provider component
- Enable JWT plugin for token generation

## Frontend JWT Handling
1. After successful login, obtain JWT from Better Auth
2. Store token in secure httpOnly cookie or localStorage (securely)
3. Attach token to all API requests via `Authorization: Bearer <token>` header
4. Implement token refresh mechanism
5. Handle token expiration gracefully

## Backend FastAPI JWT Verification (Using JWKS)
1. Create JWT dependency using PyJWT and cryptography
2. Extract token from Authorization header
3. Fetch JWKS from Better Auth's `/api/auth/jwks` endpoint
4. Verify token signature using the public key from JWKS
5. Decode payload to extract user_id
6. Use user_id to filter database queries
7. Return 401 for invalid tokens, 403 for unauthorized access

## Environment Variables
- `BETTER_AUTH_URL`: Base URL for Better Auth instance
- `DATABASE_URL`: Neon PostgreSQL connection string
- `JWT_ISSUER`: Issuer URL for token validation (should match Better Auth URL)

## Security Benefits Table

| Benefit | Implementation | Result |
|---------|----------------|---------|
| Stateless Authentication | JWT tokens contain user info | No server-side session storage needed |
| User Isolation | user_id extracted from JWT | Natural task scoping to users |
| Security | JWKS-based signature verification | Asymmetric key security, no shared secrets |
| Scalability | No session store required | Horizontal scaling simplified |
| Key Rotation | JWKS allows key rotation | Automatic key updates without configuration changes |