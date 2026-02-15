'use client';

import { useState, useEffect } from 'react';
import { getToken } from '@/lib/auth-utils';

interface TaskStatsProps {
  userId: string;
}

interface Stats {
  total: number;
  completed: number;
  pending: number;
}

export default function TaskStats({ userId }: TaskStatsProps) {
  const [stats, setStats] = useState<Stats>({ total: 0, completed: 0, pending: 0 });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchStats();
  }, [userId]);

  const fetchStats = async () => {
    try {
      setLoading(true);

      // Get authentication token
      const token = getToken();
      if (!token) {
        throw new Error('Authentication token not found');
      }

      const BACKEND_API_BASE = process.env.NEXT_PUBLIC_BACKEND_API_URL || 'http://127.0.0.1:8000';
      const response = await fetch(`${BACKEND_API_BASE}/api/${userId}/tasks`, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });

      if (!response.ok) {
        if (response.status === 401 || response.status === 403) {
          // Authentication failed, redirect to login
          localStorage.removeItem('better-auth-session-token');
          window.location.href = '/login';
          throw new Error('Authentication failed');
        }
        throw new Error('Failed to fetch tasks');
      }

      const tasks = await response.json();
      const completedCount = tasks.filter((task: any) => task.completed).length;
      const totalCount = tasks.length;

      setStats({
        total: totalCount,
        completed: completedCount,
        pending: totalCount - completedCount
      });
    } catch (err) {
      console.error('Error fetching stats:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-white p-4 rounded shadow animate-pulse">
          <div className="h-4 bg-gray-200 rounded w-3/4"></div>
          <div className="h-8 bg-gray-200 rounded mt-2"></div>
        </div>
        <div className="bg-white p-4 rounded shadow animate-pulse">
          <div className="h-4 bg-gray-200 rounded w-3/4"></div>
          <div className="h-8 bg-gray-200 rounded mt-2"></div>
        </div>
        <div className="bg-white p-4 rounded shadow animate-pulse">
          <div className="h-4 bg-gray-200 rounded w-3/4"></div>
          <div className="h-8 bg-gray-200 rounded mt-2"></div>
        </div>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-lg font-medium text-gray-500">Total Tasks</h3>
        <p className="text-3xl font-bold text-gray-900">{stats.total}</p>
      </div>
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-lg font-medium text-gray-500">Completed</h3>
        <p className="text-3xl font-bold text-green-600">{stats.completed}</p>
      </div>
      <div className="bg-white p-4 rounded shadow">
        <h3 className="text-lg font-medium text-gray-500">Pending</h3>
        <p className="text-3xl font-bold text-yellow-600">{stats.pending}</p>
      </div>
    </div>
  );
}