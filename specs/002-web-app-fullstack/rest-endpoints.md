# REST API Endpoints

## API Endpoint Specifications

| Method | Path | Description | Authentication | Request Body | Response |
|--------|------|-------------|----------------|--------------|----------|
| GET | `/api/{user_id}/tasks` | Retrieve all tasks for a specific user | JWT Required | None | Array of Task objects |
| POST | `/api/{user_id}/tasks` | Create a new task for a specific user | JWT Required | `{ "title": "string", "description": "string" }` | Created Task object |
| GET | `/api/{user_id}/tasks/{id}` | Retrieve a specific task by ID | JWT Required | None | Task object |
| PUT | `/api/{user_id}/tasks/{id}` | Update a specific task by ID | JWT Required | `{ "title": "string", "description": "string" }` | Updated Task object |
| DELETE | `/api/{user_id}/tasks/{id}` | Delete a specific task by ID | JWT Required | None | Empty response (204) |
| PATCH | `/api/{user_id}/tasks/{id}/complete` | Toggle task completion status | JWT Required | `{ "completed": true/false }` | Updated Task object |

## Authentication Details
- All endpoints require a valid JWT token in the Authorization header: `Authorization: Bearer {token}`
- User ID in the path must match the user ID in the JWT token for authorization
- Requests with mismatched user IDs will result in 403 Forbidden response

## Request/Response Format
- Content-Type: `application/json` for all requests
- Responses include standard HTTP status codes (200, 201, 204, 400, 401, 403, 404, 500)
- Error responses follow format: `{ "detail": "error message" }`
- Success responses return Task objects in format: `{ "id": number, "title": "string", "description": "string", "completed": boolean, "user_id": number, "created_at": "timestamp", "updated_at": "timestamp" }`

## User Isolation
- Each endpoint verifies that the requested user_id matches the authenticated user
- Users cannot access, modify, or delete tasks belonging to other users
- 403 Forbidden returned for unauthorized access attempts