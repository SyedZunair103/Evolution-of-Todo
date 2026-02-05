'use client';

import { useEffect, useState } from 'react';
import { useTaskApi } from '@/hooks/useTaskApi';
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

export default function TaskListWithActions({ userId }: { userId: number }) {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [editingTaskId, setEditingTaskId] = useState<number | null>(null);
  const [editTitle, setEditTitle] = useState('');
  const [editDescription, setEditDescription] = useState('');

  const {
    fetchTasks,
    updateTask,
    deleteTask,
    toggleTaskCompletion,
    loading,
    error
  } = useTaskApi();

  const loadTasks = async () => {
    const token = getToken();
    if (!token) {
      console.error('No authentication token found!');
      return;
    }

    const fetchedTasks = await fetchTasks(userId);
    if (fetchedTasks) {
      setTasks(fetchedTasks);
    }
  };

  useEffect(() => {
    loadTasks();
  }, [userId]);

  const handleDelete = async (taskId: number) => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      const token = getToken();
      if (!token) {
        alert('You are not authenticated. Please log in.');
        return;
      }

      const success = await deleteTask(userId, taskId);
      if (success) {
        setTasks(tasks.filter(task => task.id !== taskId));
      } else {
        alert('Failed to delete task');
      }
    }
  };

  const handleToggleCompletion = async (taskId: number, currentCompleted: boolean) => {
    const token = getToken();
    if (!token) {
      alert('You are not authenticated. Please log in.');
      return;
    }

    const updatedTask = await toggleTaskCompletion(userId, taskId, !currentCompleted);
    if (updatedTask) {
      setTasks(tasks.map(task =>
        task.id === taskId ? { ...task, completed: !currentCompleted } : task
      ));
    } else {
      alert('Failed to update task completion status');
    }
  };

  const startEditing = (task: Task) => {
    setEditingTaskId(task.id);
    setEditTitle(task.title);
    setEditDescription(task.description);
  };

  const handleSaveEdit = async (taskId: number) => {
    const token = getToken();
    if (!token) {
      alert('You are not authenticated. Please log in.');
      return;
    }

    const updatedTask = await updateTask(userId, taskId, {
      title: editTitle,
      description: editDescription
    });

    if (updatedTask) {
      setTasks(tasks.map(task =>
        task.id === taskId ? { ...task, title: editTitle, description: editDescription } : task
      ));
      setEditingTaskId(null);
    } else {
      alert('Failed to update task');
    }
  };

  const handleCancelEdit = () => {
    setEditingTaskId(null);
  };

  if (loading) return <p className="p-4 text-black">Loading tasks...</p>;

  if (error) {
    return <p className="p-4 text-red-600">Error: {error}</p>;
  }

  return (
    <div className="bg-white rounded shadow text-black overflow-hidden">
      {tasks.length === 0 ? (
        <p className="p-4">No tasks found.</p>
      ) : (
        <ul className="divide-y divide-gray-200">
          {tasks.map((task) => (
            <li key={task.id} className="p-4 hover:bg-gray-50 transition-colors">
              {editingTaskId === task.id ? (
                // Edit mode
                <div className="space-y-3">
                  <input
                    type="text"
                    value={editTitle}
                    onChange={(e) => setEditTitle(e.target.value)}
                    className="w-full p-2 border rounded mb-2 bg-white text-black"
                    required
                  />
                  <textarea
                    value={editDescription}
                    onChange={(e) => setEditDescription(e.target.value)}
                    className="w-full p-2 border rounded mb-2 bg-white text-black"
                  />
                  <div className="flex space-x-2">
                    <button
                      onClick={() => handleSaveEdit(task.id)}
                      className="bg-green-600 text-white py-1 px-3 rounded hover:bg-green-700"
                    >
                      Save
                    </button>
                    <button
                      onClick={handleCancelEdit}
                      className="bg-gray-500 text-white py-1 px-3 rounded hover:bg-gray-600"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              ) : (
                // Display mode
                <div className="flex items-start justify-between">
                  <div className="flex items-start space-x-3">
                    <input
                      type="checkbox"
                      checked={task.completed}
                      onChange={() => handleToggleCompletion(task.id, task.completed)}
                      className="mt-1 h-5 w-5 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                    />
                    <div>
                      <h3 className={`font-bold ${task.completed ? 'line-through text-gray-500' : ''}`}>
                        {task.title}
                      </h3>
                      {task.description && (
                        <p className={`mt-1 text-sm ${task.completed ? 'text-gray-400' : 'text-gray-600'}`}>
                          {task.description}
                        </p>
                      )}
                      <p className="mt-1 text-xs text-gray-500">
                        Created: {new Date(task.created_at).toLocaleString()}
                      </p>
                    </div>
                  </div>
                  <div className="flex space-x-2">
                    <button
                      onClick={() => startEditing(task)}
                      className="text-blue-600 hover:text-blue-800"
                      title="Edit task"
                    >
                      ✏️
                    </button>
                    <button
                      onClick={() => handleDelete(task.id)}
                      className="text-red-600 hover:text-red-800"
                      title="Delete task"
                    >
                      🗑️
                    </button>
                  </div>
                </div>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}