from task_manager import TaskManager

def initialize_tasks():
    """Initialize the tasks.json file if it doesn't exist."""
    import os
    import json
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump([], file)

def main():
    # Initialize the tasks.json file
    initialize_tasks()

    # Initialize the TaskManager
    task_manager = TaskManager("tasks.json")

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View All Tasks")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_manager.add_task(description, due_date)
            print("Task added successfully!")

        elif choice == "2":
            task_id = input("Enter the ID of the task to complete: ")
            if task_manager.complete_task(task_id):
                print("Task completed successfully!")
            else:
                print("Task not found.")

        elif choice == "3":
            tasks = task_manager.get_all_tasks()
            if tasks:
                print("\nAll Tasks:")
                for task in tasks:
                    status = "Completed" if task["completed"] else "Pending"
                    print(f"ID: {task['id']}, Description: {task['description']}, Due Date: {task['due_date']}, Status: {status}")
            else:
                print("No tasks available.")

        elif choice == "4":
            task_id = input("Enter the ID of the task to delete: ")
            if task_manager.delete_task(task_id):
                print("Task deleted successfully!")
            else:
                print("Task not found.")

        elif choice == "5":
            print("Exiting the Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()