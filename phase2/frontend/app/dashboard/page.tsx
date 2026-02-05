'use client';

import { useState, useEffect } from 'react';
import TaskForm from '@/components/TaskForm';
import TaskListWithActions from '@/components/TaskListWithActions';
import Link from 'next/link';
import AnimatedBackground from '@/components/AnimatedBackground';

export default function DashboardPage() {
  const [currentUser, setCurrentUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is logged in
    const isLoggedIn = localStorage.getItem('isLoggedIn');
    const user = localStorage.getItem('currentUser');

    console.log('Dashboard - isLoggedIn:', isLoggedIn);
    console.log('Dashboard - currentUser:', user);

    if (isLoggedIn === 'true' && user) {
      const userData = JSON.parse(user);
      console.log('Dashboard - parsed user data:', userData);
      setCurrentUser(userData);
    } else {
      // Redirect to login if not logged in (in a real app, you'd use Next.js router)
      console.log('Dashboard - Redirecting to login, not logged in');
      window.location.href = '/login';
    }

    setLoading(false);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('isLoggedIn');
    localStorage.removeItem('currentUser');
    window.location.href = '/login';
  };

  if (loading) {
    return (
      <div className="relative min-h-screen">
        <AnimatedBackground />
        <div className="flex items-center justify-center min-h-screen">Loading...</div>
      </div>
    );
  }

  if (!currentUser) {
    return null; // Redirect is happening in useEffect
  }

  return (
    <div className="relative min-h-screen">
      <AnimatedBackground />
      <div className="min-h-screen">
        <nav className="bg-white/90 backdrop-blur-sm shadow z-10 relative">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex">
                <div className="flex-shrink-0 flex items-center">
                  <span className="text-xl font-bold text-indigo-600">Todo App</span>
                </div>
                <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
                  <Link href="/dashboard" className="border-indigo-500 text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
                    Dashboard
                  </Link>
                </div>
              </div>
              <div className="flex items-center">
                <div className="ml-3 relative">
                  <div className="text-sm">
                    <span className="text-gray-700">Welcome, {currentUser.name}</span>
                  </div>
                  <button
                    onClick={handleLogout}
                    className="ml-4 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                  >
                    Logout
                  </button>
                </div>
              </div>
            </div>
          </div>
        </nav>

        <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8 relative z-10">
          <div className="px-4 py-6 sm:px-0">
            <div className="pb-5 border-b border-gray-200 sm:flex sm:items-center sm:justify-between">
              <h3 className="text-lg leading-6 font-medium text-gray-900">My Tasks</h3>
            </div>
            <div className="mt-4">
              <TaskForm userId={currentUser.id} />
              <TaskListWithActions userId={currentUser.id} />
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}