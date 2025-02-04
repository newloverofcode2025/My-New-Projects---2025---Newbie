import os
import json
import uuid
from datetime import datetime
from typing import List, Dict

class Task:
    def __init__(self, description: str, due_date: str):
        self.id = str(uuid.uuid4())  # Generate a unique ID for each task
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed,
            "timestamp": self.timestamp
        }

class TodoManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.tasks: List[Dict] = self.load_tasks()

    def add_task(self, description: str, due_date: str) -> None:
        """Add a new task."""
        new_task = Task(description, due_date)
        self.tasks.append(new_task.to_dict())
        self.save_tasks()

    def mark_task_complete(self, task_id: str) -> bool:
        """Mark a task as complete by its ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                return True
        return False

    def get_all_tasks(self) -> List[Dict]:
        """Return all tasks."""
        return self.tasks

    def delete_task(self, task_id: str) -> bool:
        """Delete a task by its ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                return True
        return False

    def save_tasks(self) -> None:
        """Save tasks to a file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self) -> List[Dict]:
        """Load tasks from a file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []