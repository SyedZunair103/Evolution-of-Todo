# Frontend Development Guidelines

## Tech Stack
- Next.js 16+ with App Router
- React Server Components and Client Components as appropriate
- Tailwind CSS for styling
- Shadcn/ui components for consistent UI elements
- Better Auth for authentication
- Axios or fetch for API calls

## File Structure
- `app/` - Next.js App Router pages
- `components/` - Reusable UI components
- `lib/` - Utility functions and constants
- `styles/` - Global styles and Tailwind configuration
- `public/` - Static assets

## API Integration
- Use BETTER_AUTH_SECRET for JWT validation consistency
- Implement proper error handling for API responses
- Show loading states during API requests
- Implement proper form validation before submitting

## Authentication Flow
- Integrate Better Auth for login/signup forms
- Use JWT tokens from Better Auth for API authentication
- Protect routes that require authentication
- Implement proper logout functionality