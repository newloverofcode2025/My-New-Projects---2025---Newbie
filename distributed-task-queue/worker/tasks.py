from celery import Celery  
import time  

app = Celery(  
    'tasks',  
    broker='redis://redis:6379/0',  
    backend='redis://redis:6379/0'  
)  

@app.task(bind=True, max_retries=3)  
def process_task(self, data: str):  
    try:  
        # Simulate work (replace with actual logic)  
        time.sleep(5)  
        if "fail" in data:  
            raise ValueError("Simulated failure")  
        return f"Processed: {data.upper()}"  
    except Exception as e:  
        self.retry(exc=e, countdown=30)  