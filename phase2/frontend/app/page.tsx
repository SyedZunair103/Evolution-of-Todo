'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import AnimatedBackground from '@/components/AnimatedBackground';

export default function HomePage() {
  const router = useRouter();

  return (
    <div className="relative min-h-screen">
      <AnimatedBackground />
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-center z-10 relative">
          <h1 className="text-3xl font-bold text-gray-800 mb-4">Todo App</h1>
          <p className="text-lg text-gray-600 mb-8">Manage your tasks efficiently</p>

          <div className="space-x-4">
            <Link
              href="/login"
              className="inline-block bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-2 px-6 rounded-md transition duration-300"
            >
              Sign In
            </Link>
            <Link
              href="/signup"
              className="inline-block bg-white hover:bg-gray-100 text-indigo-600 font-medium py-2 px-6 rounded-md border border-indigo-600 transition duration-300"
            >
              Sign Up
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}