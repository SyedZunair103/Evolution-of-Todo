'use client';
import { useEffect, useState } from 'react';
import { getToken } from '@/lib/auth-utils';

export default function TaskList({ userId }: { userId: number }) {
  const [tasks, setTasks] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const BACKEND_API_BASE = process.env.NEXT_PUBLIC_BACKEND_API_URL || 'http://127.0.0.1:8000';

  const fetchTasks = async () => {
    try {
      const token = getToken();

      console.log('Fetching tasks from:', `${BACKEND_API_BASE}/api/${userId}/tasks`);
      console.log('Using token:', token ? 'Yes' : 'No');
      console.log('Using userId:', userId);

      if (!token) {
        console.error('No authentication token found!');
        return; // Just return without making the API call
      }

      const response = await fetch(`${BACKEND_API_BASE}/api/${userId}/tasks`, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });

      console.log('Response status:', response.status);

      if (response.ok) {
        const data = await response.json();
        setTasks(data);
      } else if (response.status === 401 || response.status === 403) {
        const errorData = await response.json().catch(() => ({ detail: 'Authentication failed' }));
        console.error('Authentication error:', errorData);
        // Optionally redirect to login
        console.log('Authentication failed, redirecting to login...');
        localStorage.removeItem('better-auth-session-token');
        localStorage.removeItem('isLoggedIn');
        window.location.href = '/login';
      } else {
        const errorText = await response.text();
        console.error('API Error:', errorText);
        alert(`Failed to fetch tasks: ${errorText || 'API error occurred'}`);
      }
    } catch (err) {
      console.error('Network error when fetching tasks:', err);
      alert('Unable to connect to the backend server. Please make sure the backend is running on http://127.0.0.1:8000');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const fetchTasksWrapper = async () => {
      // Check if user is authenticated before attempting to fetch tasks
      const token = getToken();
      if (!token) {
        console.log('No token found, skipping task fetch');
        return;
      }

      await fetchTasks();
    };

    fetchTasksWrapper();
  }, [userId]);

  if (loading) return <p className="p-4 text-black">Loading...</p>;

  return (
    <div className="bg-white rounded shadow text-black">
      {tasks.length === 0 ? <p className="p-4">No tasks found.</p> : (
        <ul className="divide-y">
          {tasks.map((t: any) => (
            <li key={t.id} className="p-4 font-bold">{t.title}</li>
          ))}
        </ul>
      )}
    </div>
  );
}