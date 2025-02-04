from todo_manager import TodoManager

def initialize_tasks():
    """Initialize the tasks.json file if it doesn't exist."""
    import os
    import json
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump([], file)

def main():
    """Main function to run the To-Do List application."""
    # Initialize the tasks.json file
    initialize_tasks()

    # Initialize the TodoManager
    todo_manager = TodoManager("tasks.json")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View All Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_manager.add_task(description, due_date)
            print("Task added successfully!")

        elif choice == "2":
            task_id = input("Enter the ID of the task to mark as complete: ")
            if todo_manager.mark_task_complete(task_id):
                print("Task marked as complete!")
            else:
                print("Task not found.")

        elif choice == "3":
            tasks = todo_manager.get_all_tasks()
            if tasks:
                print("\nAll Tasks:")
                for task in tasks:
                    status = "Completed" if task["completed"] else "Pending"
                    print(f"ID: {task['id']}, Description: {task['description']}, Due Date: {task['due_date']}, Status: {status}")
            else:
                print("No tasks available.")

        elif choice == "4":
            task_id = input("Enter the ID of the task to delete: ")
            if todo_manager.delete_task(task_id):
                print("Task deleted successfully!")
            else:
                print("Task not found.")

        elif choice == "5":
            print("Exiting the To-Do List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()