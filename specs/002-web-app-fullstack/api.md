# API Specs Table

| Method | Endpoint | Description | Auth Required | Request Body | Response | Notes |
|--------|----------|-------------|---------------|--------------|----------|-------|
| POST | `/api/auth/signup` | User registration | No | `{email, password, name}` | `{user, token}` | Better Auth endpoint |
| POST | `/api/auth/signin` | User login | No | `{email, password}` | `{user, token}` | Better Auth endpoint |
| GET | `/api/users/{user_id}/tasks` | Get user's tasks | Yes (JWT) | - | `[{id, title, description, completed, created_at}]` | Filters by user_id |
| POST | `/api/users/{user_id}/tasks` | Create task | Yes (JWT) | `{title, description}` | `{id, title, description, completed, created_at}` | Sets user_id from JWT |
| GET | `/api/users/{user_id}/tasks/{task_id}` | Get specific task | Yes (JWT) | - | `{id, title, description, completed, created_at}` | Verifies ownership |
| PUT | `/api/users/{user_id}/tasks/{task_id}` | Update task | Yes (JWT) | `{title, description, completed}` | `{id, title, description, completed, updated_at}` | Verifies ownership |
| DELETE | `/api/users/{user_id}/tasks/{task_id}` | Delete task | Yes (JWT) | - | `{success: boolean}` | Verifies ownership |
| PATCH | `/api/users/{user_id}/tasks/{task_id}/toggle` | Toggle completion | Yes (JWT) | - | `{id, completed}` | Verifies ownership |

## Authentication Details
- **Header**: `Authorization: Bearer <jwt_token>`
- **Response Codes**:
  - `200` - Success
  - `401` - Missing or invalid token
  - `403` - Valid token but unauthorized for resource
  - `404` - Resource not found
- **Token Verification**: Backend decodes JWT and extracts user_id for authorization