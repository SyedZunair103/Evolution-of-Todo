# Frontend (Next.js App Router)

## Page Structure
- `/` - Landing page with login/signup links
- `/login` - Secure login form using Better Auth
- `/signup` - Registration form using Better Auth
- `/dashboard` - Protected route with task management UI

## Component Structure
- `components/auth/LoginForm.tsx` - Email/password login form
- `components/auth/SignupForm.tsx` - Registration form
- `components/tasks/TaskList.tsx` - Displays user's tasks
- `components/tasks/TaskCard.tsx` - Individual task display
- `components/tasks/TaskForm.tsx` - Add/edit task form
- `components/tasks/ToggleButton.tsx` - Complete/incomplete toggle
- `components/layout/Header.tsx` - Navigation and user controls
- `components/layout/ProtectedRoute.tsx` - Authentication wrapper

## Protection Mechanisms
- Server-side: `cookies().get("better-auth.session_token")` in layout/page functions
- Client-side: React Context Provider with auth state
- API calls: Interceptor that adds Authorization header
- Redirect: Middleware to redirect unauthenticated users

## UI Recommendations
- **Styling**: Tailwind CSS with custom configuration
- **Components**: Use shadcn/ui for accessible, well-designed components
- **Forms**: React Hook Form with Zod validation
- **State**: Zustand or React Context for global state
- **API**: Axios or native fetch with interceptors

## shadcn/ui + Tailwind Benefits
- Rapid development with pre-built, accessible components
- Consistent design system across the application
- Responsive by default with Tailwind utility classes
- Easy customization with CSS variables
- Strong accessibility built-in
- Active community and frequent updates