from fastapi import FastAPI, HTTPException
from typing import List, Dict

app = FastAPI()

# Sample data to store tasks
tasks: List[Dict[str, str]] = []


@app.post("/tasks/", response_model=Dict[str, str])
async def create_task(task: Dict[str, str]):
    tasks.append(task)
    return task


@app.get("/tasks/", response_model=List[Dict[str, str]])
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Dict[str, str])
async def get_task(task_id: int):
    if 0 <= task_id < len(tasks):
        return tasks[task_id]
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Dict[str, str])
async def update_task(task_id: int, updated_task: Dict[str, str]):
    if 0 <= task_id < len(tasks):
        tasks[task_id] = updated_task
        return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", response_model=Dict[str, str])
async def delete_task(task_id: int):
    if 0 <= task_id < len(tasks):
        deleted_task = tasks.pop(task_id)
        return deleted_task
    raise HTTPException(status_code=404, detail="Task not found")
