import { useState } from 'react';
import { getToken } from '@/lib/auth-utils';

interface Task {
  id: number;
  user_id: number;
  title: string;
  description: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
}

interface TaskApiResult {
  loading: boolean;
  error: string | null;
  createTask: (userId: number, taskData: { title: string; description: string }) => Promise<Task | null>;
  fetchTasks: (userId: number) => Promise<Task[] | null>;
  updateTask: (userId: number, taskId: number, taskData: Partial<{ title: string; description: string; completed: boolean }>) => Promise<Task | null>;
  deleteTask: (userId: number, taskId: number) => Promise<boolean>;
  toggleTaskCompletion: (userId: number, taskId: number, completed: boolean) => Promise<Task | null>;
}

export const useTaskApi = (): TaskApiResult => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const executeRequest = async <T>(
    url: string,
    options: RequestInit = {}
  ): Promise<T | null> => {
    setLoading(true);
    setError(null);

    // Construct full API URL using environment variable
    const BACKEND_API_BASE = process.env.NEXT_PUBLIC_BACKEND_API_URL || 'http://127.0.0.1:8000';
    const fullUrl = `${BACKEND_API_BASE}${url}`;

    // Get authentication token
    const token = getToken();
    if (!token) {
      setError('Authentication token not found. Please log in.');
      setLoading(false);
      return null;
    }

    try {
      const response = await fetch(fullUrl, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`, // Add authentication token
          ...options.headers,
        },
        ...options,
      });

      if (!response.ok) {
        if (response.status === 401 || response.status === 403) {
          setError('Authentication failed. Please log in again.');
          // Optionally clear token and redirect to login
          localStorage.removeItem('better-auth-session-token');
          window.location.href = '/login';
        }
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'An error occurred';
      setError(errorMessage);
      return null;
    } finally {
      setLoading(false);
    }
  };

  const createTask = async (
    userId: number,
    taskData: { title: string; description: string }
  ): Promise<Task | null> => {
    return executeRequest<Task>(`/api/${userId}/tasks`, {
      method: 'POST',
      body: JSON.stringify({
        ...taskData,
        user_id: userId,
        completed: false
      })
    });
  };

  const fetchTasks = async (userId: number): Promise<Task[] | null> => {
    return executeRequest<Task[]>(`/api/${userId}/tasks`);
  };

  const updateTask = async (
    userId: number,
    taskId: number,
    taskData: Partial<{ title: string; description: string; completed: boolean }>
  ): Promise<Task | null> => {
    return executeRequest<Task>(`/api/${userId}/tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(taskData)
    });
  };

  const deleteTask = async (userId: number, taskId: number): Promise<boolean> => {
    const result = await executeRequest(`/api/${userId}/tasks/${taskId}`, {
      method: 'DELETE'
    });
    return result !== null;
  };

  const toggleTaskCompletion = async (
    userId: number,
    taskId: number,
    completed: boolean
  ): Promise<Task | null> => {
    return executeRequest<Task>(`/api/${userId}/tasks/${taskId}/complete`, {
      method: 'PATCH',
      body: JSON.stringify({ completed })
    });
  };

  return {
    loading,
    error,
    createTask,
    fetchTasks,
    updateTask,
    deleteTask,
    toggleTaskCompletion
  };
};