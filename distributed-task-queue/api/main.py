from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from celery import Celery
import requests

app = FastAPI()

celery = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

class TaskRequest(BaseModel):
    data: str  # Could be image URL, text, etc.
    priority: int = 1

@app.post("/tasks")
def create_task(request: TaskRequest):
    task_id = str(uuid.uuid4())
    celery.send_task(
        "worker.process_task",
        args=[request.data],
        task_id=task_id,
        priority=request.priority
    )
    return {"task_id": task_id}

url = "http://127.0.0.1:8000/tasks"
data = {
    "data": "example_data",
    "priority": 1
}

response = requests.post(url, json=data)
print(response.json())