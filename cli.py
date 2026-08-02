from typing import Optional

from manager import TaskManager
from storage import TaskStorage
from models import Task


def print_menu() -> None:
    print("\n=== To-Do List Manager ===")
    print("1. Add task")
    print("2. List all tasks")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. Edit task")
    print("6. Filter tasks")
    print("7. Search tasks")
    print("8. Show stats")
    print("9. Exit")


def get_non_empty_string(prompt: str) -> str:
    """Read a non-empty string from user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_optional_string(prompt: str) -> str:
    """Read an optional string (can be empty)."""
    return input(prompt).strip()


def get_int_input(prompt: str) -> Optional[int]:
    value = input(prompt).strip()
    if not value:
        return None
    if not value.isdigit():
        return None
    return int(value)


def display_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("No tasks found.")
        return

    print(
        "\nID  | Title                | Status  | Priority | Due Date   | Category   | Created at"
    )
    print("-" * 95)
    for task in tasks:
        status = "Done" if task.completed else "Pending"
        title_short = (task.title[:20] + "...") if len(task.title) > 23 else task.title
        due = task.due_date if task.due_date else "-"
        cat = task.category if task.category else "General"
        print(
            f"{task.id:<3} | {title_short:<20} | {status:<7} | {task.priority:<8} | {due:<10} | {cat:<10} | {task.created_at}"
        )


def main() -> None:
    storage = TaskStorage("tasks.json")
    manager = TaskManager(storage)

    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            # Add task
            title = get_non_empty_string("Enter task title: ")
            description = get_optional_string("Enter task description (optional): ")
            due_date = get_optional_string("Enter due date (YYYY-MM-DD, optional): ")

            print("Choose priority:")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            priority_choice = input("Enter priority choice (1-3, default=2): ").strip()
            if priority_choice == "1":
                priority = "Low"
            elif priority_choice == "3":
                priority = "High"
            else:
                priority = "Medium"

            print("Choose category:")
            print("1. Study")
            print("2. Work")
            print("3. Personal")
            print("4. General (default)")
            category_choice = input("Enter category choice (1-4, default=4): ").strip()
            if category_choice == "1":
                category = "Study"
            elif category_choice == "2":
                category = "Work"
            elif category_choice == "3":
                category = "Personal"
            else:
                category = "General"

            task = manager.add_task(
                title=title,
                description=description,
                due_date=due_date,
                priority=priority,
                category=category,
            )
            print(f"Task added with ID {task.id}.")

        elif choice == "2":
            # List all tasks
            tasks = manager.list_tasks()
            display_tasks(tasks)

        elif choice == "3":
            # Complete task
            task_id = get_int_input("Enter task ID to complete: ")
            if task_id is None:
                print("Error: Please enter a valid numeric ID.")
                continue
            if manager.complete_task(task_id):
                print(f"Task {task_id} marked as completed.")
            else:
                print(f"Task with ID {task_id} not found.")

        elif choice == "4":
            # Remove task
            task_id = get_int_input("Enter task ID to remove: ")
            if task_id is None:
                print("Error: Please enter a valid numeric ID.")
                continue
            confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").strip().lower()
            if confirm != "y":
                print("Deletion cancelled.")
                continue
            if manager.remove_task(task_id):
                print(f"Task {task_id} removed.")
            else:
                print(f"Task with ID {task_id} not found.")

        elif choice == "5":
            # Edit task
            task_id = get_int_input("Enter task ID to edit: ")
            if task_id is None:
                print("Error: Please enter a valid numeric ID.")
                continue

            task = manager.find_task(task_id)
            if task is None:
                print(f"Task with ID {task_id} not found.")
                continue

            print(f"Editing task {task_id}:")
            print(f"Current title: {task.title}")
            new_title = get_optional_string("Enter new title (leave empty to keep same): ")
            if new_title:
                task.title = new_title

            print(f"Current description: {task.description}")
            new_description = get_optional_string("Enter new description (leave empty to keep same): ")
            if new_description:
                task.description = new_description

            print(f"Current due date: {task.due_date or '(none)'}")
            new_due_date = get_optional_string("Enter new due date (YYYY-MM-DD, leave empty to keep same): ")
            if new_due_date:
                task.due_date = new_due_date

            print(f"Current priority: {task.priority}")
            print("Choose new priority (or leave empty to keep same):")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            new_priority_choice = input("Enter priority choice (1-3, or empty to keep same): ").strip()
            if new_priority_choice == "1":
                task.priority = "Low"
            elif new_priority_choice == "3":
                task.priority = "High"
            elif new_priority_choice == "2":
                task.priority = "Medium"

            print(f"Current category: {task.category}")
            print("Choose new category (or leave empty to keep same):")
            print("1. Study")
            print("2. Work")
            print("3. Personal")
            print("4. General")
            new_category_choice = input("Enter category choice (1-4, or empty to keep same): ").strip()
            if new_category_choice == "1":
                task.category = "Study"
            elif new_category_choice == "2":
                task.category = "Work"
            elif new_category_choice == "3":
                task.category = "Personal"
            elif new_category_choice == "4":
                task.category = "General"

            manager._storage.save_tasks(manager._tasks)
            print(f"Task {task_id} updated.")

        elif choice == "6":
            # Filter tasks
            print("Filter by status:")
            print("1. All")
            print("2. Pending")
            print("3. Completed")
            filter_choice = input("Enter choice (1-3): ").strip()

            if filter_choice == "1":
                status = "all"
            elif filter_choice == "2":
                status = "pending"
            elif filter_choice == "3":
                status = "completed"
            else:
                print("Invalid choice.")
                continue

            tasks = manager.filter_tasks(status)
            display_tasks(tasks)

        elif choice == "7":
            # Search tasks
            search_text = input("Enter text to search in task titles: ").strip()
            if not search_text:
                print("Search text cannot be empty.")
                continue

            tasks = manager.search_tasks(search_text)
            if not tasks:
                print("No tasks found matching that text.")
            else:
                display_tasks(tasks)

        elif choice == "8":
            # Show stats
            stats = manager.get_stats()
            print("\n=== Task Statistics ===")
            print(f"Total tasks   : {stats['total']}")
            print(f"Completed     : {stats['completed']}")
            print(f"Pending       : {stats['pending']}")

        elif choice == "9":
            # Exit
            print("Exiting To-Do List Manager. Goodbye!")
            break

        else:
            # Invalid choice
            print("Invalid choice. Please select a number between 1 and 9.")


if __name__ == "__main__":
    main()