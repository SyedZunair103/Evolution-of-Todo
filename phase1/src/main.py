"""
Main entry point for the Todo CLI Application.

This module runs the main application loop and orchestrates the CLI interface.
"""

from .storage import InMemoryStore
from .cli import (
    display_menu,
    get_user_choice,
    display_add_task,
    display_view_tasks,
    display_update_task,
    display_delete_task,
    display_toggle_task
)


def main():
    """Main application entry point."""
    store = InMemoryStore()

    print("Welcome to the Todo CLI Application!")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            display_add_task(store)
        elif choice == 2:
            display_view_tasks(store)
        elif choice == 3:
            display_update_task(store)
        elif choice == 4:
            display_delete_task(store)
        elif choice == 5:
            display_toggle_task(store)
        elif choice == 0:
            print("Thank you for using the Todo CLI Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Pause before showing the menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()