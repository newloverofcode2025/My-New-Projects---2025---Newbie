import json
import os
import uuid

class Task:
    def __init__(self, description, due_date):
        self.id = str(uuid.uuid4())  # Generate a unique ID for each task
        self.description = description
        self.due_date = due_date
        self.completed = False

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description, due_date):
        """Add a new task."""
        new_task = Task(description, due_date)
        self.tasks.append(new_task.to_dict())
        self.save_tasks()

    def mark_task_complete(self, task_id):
        """Mark a task as complete by its ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                return True
        return False

    def get_all_tasks(self):
        """Return all tasks."""
        return self.tasks

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                return True
        return False