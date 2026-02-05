'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import AnimatedBackground from '@/components/AnimatedBackground';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      const BACKEND_API_BASE = process.env.NEXT_PUBLIC_BACKEND_API_URL || 'http://127.0.0.1:8000';
      const response = await fetch(`${BACKEND_API_BASE}/api/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          password: password
        })
      });

      if (response.ok) {
        const data = await response.json();
        const token = data.token; // Get the actual token from backend

        // Save the actual token and user info using the same key as LoginForm component
        localStorage.setItem('better-auth-session-token', token);
        document.cookie = `better-auth.session_token=${token}; path=/; max-age=86400; SameSite=Strict;`;
        localStorage.setItem('isLoggedIn', 'true');

        // Save user info from the response or create from email
        const user = data.user || {
          id: 1,
          email: email,
          name: email.split('@')[0]
        };

        localStorage.setItem('currentUser', JSON.stringify(user));

        console.log("Login Successful!");
        router.push('/dashboard');
      } else {
        const errorData = await response.json();
        const typedErrorData = errorData as any;
        alert(typedErrorData.detail || 'Login failed');
      }
    } catch (error) {
      console.error('Login error:', error);
      alert('Connection error. Please make sure the backend server is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="relative min-h-screen">
      <AnimatedBackground />
      <div className="min-h-screen flex items-center justify-center p-4">
        <div className="max-w-md w-full bg-white/90 backdrop-blur-sm p-8 rounded-lg shadow-xl z-10">
          <h2 className="text-2xl font-bold text-center text-gray-900 mb-8">Sign In</h2>
          <form onSubmit={handleSubmit} className="space-y-6">
            <input
              type="email"
              placeholder="Email address"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none text-black"
            />
            <input
              type="password"
              placeholder="Password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none text-black"
            />
            <button
              type="submit"
              className="w-full py-2 px-4 bg-indigo-600 hover:bg-indigo-700 text-white font-medium rounded-md"
            >
              {loading ? 'Processing...' : 'Sign in'}
            </button>
          </form>
          <div className="mt-6 text-center">
            <p className="text-sm text-gray-600">
              Don't have an account?{' '}
              <a href="/signup" className="font-medium text-indigo-600 hover:text-indigo-500">
                Sign up
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}