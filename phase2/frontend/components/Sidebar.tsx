import Link from 'next/link';

interface SidebarProps {
  isOpen: boolean;
  toggleSidebar: () => void;
}

export default function Sidebar({ isOpen, toggleSidebar }: SidebarProps) {
  return (
    <>
      {/* Mobile sidebar */}
      <div className={`fixed inset-0 z-40 md:hidden ${isOpen ? 'block' : 'hidden'}`}>
        <div className="fixed inset-0 bg-gray-600 bg-opacity-75" onClick={toggleSidebar}></div>
        <div className="relative flex-1 flex flex-col max-w-xs w-full bg-white">
          <div className="flex-shrink-0 flex items-center px-4">
            <span className="text-xl font-bold text-indigo-600">Todo App</span>
          </div>
          <nav className="mt-5 px-2 space-y-1">
            <Link
              href="/dashboard"
              className="bg-indigo-50 text-indigo-600 group flex items-center px-2 py-2 text-base font-medium rounded-md"
              onClick={toggleSidebar}
            >
              Dashboard
            </Link>
          </nav>
        </div>
      </div>

      {/* Desktop sidebar */}
      <div className="hidden md:flex md:w-64 md:flex-col md:fixed md:inset-y-0">
        <div className="flex-1 flex flex-col min-h-0 border-r border-gray-200 bg-white">
          <div className="flex-1 flex flex-col pt-5 pb-4 overflow-y-auto">
            <div className="flex items-center justify-center">
              <span className="text-xl font-bold text-indigo-600">Todo App</span>
            </div>
            <nav className="mt-5 flex-1 px-2 space-y-1">
              <Link
                href="/dashboard"
                className="bg-indigo-50 text-indigo-600 group flex items-center px-2 py-2 text-sm font-medium rounded-md"
              >
                Dashboard
              </Link>
            </nav>
          </div>
        </div>
      </div>
    </>
  );
}