#!/usr/bin/env python3
"""
FastAPI with Pydantic Models

Demonstrates request/response validation and documentation.

Run with:
    uv run python with_pydantic_models.py
    # or
    uv run uvicorn with_pydantic_models:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Create FastAPI app
app = FastAPI(
    title="Agent Task API",
    description="FastAPI with Pydantic models",
    version="0.1.0"
)


# Define request/response models using Pydantic
class Task(BaseModel):
    """A task to be processed by an agent"""
    id: int
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: bool = False
    created_at: datetime


class TaskCreate(BaseModel):
    """Request model for creating a task"""
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)


class TaskUpdate(BaseModel):
    """Request model for updating a task"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


# In-memory database (for demonstration)
tasks_db: dict[int, Task] = {}
next_id = 1


@app.get("/tasks", response_model=List[Task])
async def list_tasks():
    """Get all tasks"""
    return list(tasks_db.values())


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Get a specific task"""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]


@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    """Create a new task"""
    global next_id
    
    new_task = Task(
        id=next_id,
        title=task.title,
        description=task.description,
        completed=False,
        created_at=datetime.now()
    )
    
    tasks_db[next_id] = new_task
    next_id += 1
    
    return new_task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Update an existing task"""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    existing_task = tasks_db[task_id]
    update_data = task_update.dict(exclude_unset=True)
    
    updated_task = existing_task.copy(update={**update_data})
    tasks_db[task_id] = updated_task
    
    return updated_task


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task"""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    del tasks_db[task_id]
    return {"message": "Task deleted"}


@app.get("/")
async def root():
    """Root endpoint with API info"""
    return {
        "app": "Agent Task API",
        "version": "0.1.0",
        "docs": "/docs",
        "endpoints": {
            "list_tasks": "GET /tasks",
            "get_task": "GET /tasks/{task_id}",
            "create_task": "POST /tasks",
            "update_task": "PUT /tasks/{task_id}",
            "delete_task": "DELETE /tasks/{task_id}"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("with_pydantic_models:app", host="0.0.0.0", port=8000, reload=True)
