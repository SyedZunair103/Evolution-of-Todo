interface DeleteConfirmationProps {
  onConfirm: () => void;
  onCancel: () => void;
  message?: string;
}

export default function DeleteConfirmation({ onConfirm, onCancel, message = "Are you sure you want to delete this item?" }: DeleteConfirmationProps) {
  return (
    <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center z-50">
      <div className="relative p-5 bg-white rounded-lg shadow-xl max-w-md w-full mx-4">
        <div className="mt-3 text-center">
          <h3 className="text-lg leading-6 font-medium text-gray-900">
            Confirm Deletion
          </h3>
          <div className="mt-2 px-7 py-3">
            <p className="text-sm text-gray-500">
              {message}
            </p>
          </div>
          <div className="items-center px-4 py-3">
            <button
              onClick={onConfirm}
              className="px-4 py-2 bg-red-500 text-white text-base font-medium rounded-md shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-300 mr-2"
            >
              Delete
            </button>
            <button
              onClick={onCancel}
              className="px-4 py-2 bg-gray-300 text-black text-base font-medium rounded-md shadow-sm hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-300"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}