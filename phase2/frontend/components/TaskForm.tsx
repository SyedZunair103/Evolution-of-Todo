'use client';
import { useState } from 'react';
import { getToken } from '@/lib/auth-utils';

export default function TaskForm({ userId, onSubmitCallback }: { userId: number, onSubmitCallback?: () => void }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(false);

  const BACKEND_API_BASE = process.env.NEXT_PUBLIC_BACKEND_API_URL || 'http://127.0.0.1:8000';

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    // Use the same auth utility as TaskList
    const token = getToken();

    console.log("Submitting task for User:", userId);
    console.log("Using Token:", token ? "Token Found" : "MISSING");

    if (!token) {
      alert("You are not authenticated. Please log in.");
      return;
    }

    try {
      const response = await fetch(`${BACKEND_API_BASE}/api/${userId}/tasks`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}` // Token header mein lazmi bhejna hai
        },
        body: JSON.stringify({
          title: title.trim(),
          description: description.trim(),
          completed: false
        }),
      });

      if (response.ok) {
        setTitle('');
        setDescription('');
        console.log("Task added successfully!");
        if (onSubmitCallback) onSubmitCallback();
        else window.location.reload();
      } else {
        let errorData = {};
        try {
          // Check if response has content before attempting to parse JSON
          const contentType = response.headers.get('content-type');
          if (contentType && contentType.includes('application/json')) {
            errorData = await response.json();
          } else {
            // If not JSON, try to get text content
            const errorText = await response.text();
            errorData = { detail: errorText || `HTTP Error: ${response.status}` };
          }
        } catch (parseError) {
          // If parsing fails, create a generic error object
          errorData = { detail: `HTTP Error: ${response.status}` };
        }

        console.error("Server Error:", errorData);

        // Handle the error data properly - it might be an object or array
        let errorMessage = 'Could not add task';

        // Type assertion to handle potentially unknown object structure
        const typedErrorData = errorData as any;

        if (typedErrorData && typeof typedErrorData === 'object') {
          if (Array.isArray(typedErrorData.detail)) {
            // Handle Pydantic validation error array
            errorMessage = typedErrorData.detail.map((err: any) => err.msg || 'Validation error').join(', ');
          } else if (typedErrorData.detail) {
            errorMessage = typedErrorData.detail;
          } else if (typedErrorData.message) {
            errorMessage = typedErrorData.message;
          } else {
            errorMessage = JSON.stringify(typedErrorData);
          }
        } else if (typeof typedErrorData === 'string') {
          errorMessage = typedErrorData;
        }

        alert(`Error: ${errorMessage}`);
      }
    } catch (err) {
      console.error("Network error when creating task:", err);
      alert("Unable to connect to the backend server. Please make sure the backend is running on http://127.0.0.1:8000");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-6 p-4 bg-white rounded shadow border text-black">
      <h3 className="text-lg font-bold mb-3">Add New Task</h3>
      <input 
        className="w-full p-2 border rounded mb-2 bg-white" 
        placeholder="Task Title" 
        value={title} 
        onChange={e => setTitle(e.target.value)} 
        required 
      />
      <textarea 
        className="w-full p-2 border rounded mb-2 bg-white" 
        placeholder="Description" 
        value={description} 
        onChange={e => setDescription(e.target.value)} 
      />
      <button 
        type="submit" 
        disabled={loading}
        className="bg-indigo-600 text-white py-2 px-4 rounded hover:bg-indigo-700 w-full disabled:bg-gray-400"
      >
        {loading ? 'Adding...' : 'Add Task'}
      </button>
    </form>
  );
}