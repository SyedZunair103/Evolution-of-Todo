# AuthAgent

## Purpose
Reusable sub-agent for JWT verification and user_id extraction (Better Auth + FastAPI backend).

## Skills
- validate_jwt(token: str) → JWKS fetch kar ke token verify kare, return payload with user_id or raise 401
- get_current_user_id() → FastAPI dependency, Bearer header se user_id nikale, 401 on invalid token

## Usage Example
@.claude/agents/auth-agent.md get current user_id from request header

## Prompt Template
"Use AuthAgent to validate JWT token and get user_id for current request."