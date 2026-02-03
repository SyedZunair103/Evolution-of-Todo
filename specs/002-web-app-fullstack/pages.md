# UI Pages

## Login Page (/login)
- Contains LoginForm with email and password fields
- Social login buttons (Google, GitHub) via Better Auth
- Link to signup page for new users
- Forgot password link
- Form validation and error messaging
- Responsive design for mobile and desktop
- Redirects to dashboard after successful login

## Signup Page (/signup)
- Contains SignupForm with email, password, and confirm password fields
- Social signup options (Google, GitHub) via Better Auth
- Terms of service and privacy policy links
- Link to login page for existing users
- Form validation and error messaging
- Responsive design for mobile and desktop
- Redirects to dashboard after successful registration

## Dashboard Page (/dashboard)
- Header with app logo and user profile dropdown
- Main content area showing TaskList component
- AddTaskButton to create new tasks
- TaskStats showing task counts
- Responsive layout with sidebar navigation (mobile hamburger menu)
- Real-time updates when tasks are modified
- Loading states during API requests
- Empty state when no tasks exist
- Logout functionality in user profile dropdown

## Page Navigation
- Protected routes: Dashboard requires authentication
- Unprotected routes: Login and Signup pages
- Automatic redirect from login/signup to dashboard when already authenticated
- Back button handling and browser history management
- Error boundary for graceful error handling