# UI Components

## Core Components

### TaskList Component
- Displays all tasks for the current user in a scrollable list
- Shows task title, description, and completion status
- Includes action buttons for each task (edit, delete, toggle complete)
- Empty state message when no tasks exist
- Sorts tasks by creation date (newest first)
- Real-time updates when tasks are added/modified/deleted

### TaskForm Component
- Form with title and description input fields
- Submit button to create or update tasks
- Form validation for required fields
- Cancel button to close the form without saving
- Success/error messages display
- Pre-populates fields when editing existing tasks

### Authentication Components
- LoginForm: Email/password fields with validation and submit button
- SignupForm: Email/password/confirm password fields with validation
- SocialLoginButtons: Google, GitHub login options (via Better Auth)
- UserProfile: Displays current user information and logout button

### Dashboard Components
- TaskStats: Shows counts of total, completed, and pending tasks
- AddTaskButton: Opens TaskForm to create new tasks
- SearchFilter: Allows filtering tasks (future extensibility)
- LoadingSpinner: Shows during API requests
- ToastNotifications: Displays success/error messages
- Header: Navigation bar with logo and user profile dropdown
- Sidebar: Navigation menu (mobile responsive)