#!/usr/bin/env python3
"""
Common Async Patterns in FastAPI

Demonstrates:
- Async/await patterns
- Background tasks
- Streaming responses
- Dependency injection

Run with:
    uv run python async_patterns.py
"""

import asyncio
from fastapi import FastAPI, BackgroundTasks, Depends
from pydantic import BaseModel
import time

app = FastAPI(title="Async Patterns Demo")


# ============================================================================
# 1. SIMPLE ASYNC ENDPOINT
# ============================================================================

@app.get("/fast")
async def fast_endpoint():
    """This doesn't block - it's async"""
    return {"status": "fast response"}


@app.get("/simulate-wait")
async def simulate_work(seconds: int = 2):
    """Simulate async work with asyncio.sleep"""
    await asyncio.sleep(seconds)
    return {"waited": f"{seconds} seconds", "status": "done"}


# ============================================================================
# 2. BACKGROUND TASKS
# ============================================================================

def log_task(task_id: int, action: str):
    """Background task - runs after response is sent"""
    time.sleep(2)  # Simulate work
    print(f"[Background] Task {task_id}: {action} completed")


@app.post("/task")
async def create_task(background_tasks: BackgroundTasks):
    """
    Endpoint that returns immediately while background task runs.
    The task runs AFTER the response is sent to the client.
    """
    background_tasks.add_task(log_task, task_id=1, action="processing")
    return {"message": "Task queued", "status": "submitted"}


# ============================================================================
# 3. DEPENDENCY INJECTION
# ============================================================================

class Config:
    """Configuration dependency"""
    def __init__(self):
        self.api_key = "secret-key-123"
        self.timeout = 30


def get_config():
    """Dependency that provides config"""
    return Config()


@app.get("/config")
async def get_api_config(config: Config = Depends(get_config)):
    """Endpoint that uses dependency injection"""
    return {
        "timeout": config.timeout,
        "api_key": "***"  # Never expose in real app!
    }


# ============================================================================
# 4. STREAMING RESPONSES
# ============================================================================

async def generate_items():
    """Async generator for streaming"""
    for i in range(5):
        await asyncio.sleep(0.5)  # Simulate work
        yield f'{{"index": {i}, "message": "chunk {i}"}}\n'


@app.get("/stream")
async def stream_endpoint():
    """Stream responses line by line"""
    from fastapi.responses import StreamingResponse
    
    return StreamingResponse(
        generate_items(),
        media_type="application/json"
    )


# ============================================================================
# 5. CONCURRENT ASYNC OPERATIONS
# ============================================================================

async def fetch_data(endpoint: str, delay: int):
    """Simulate fetching data from external service"""
    await asyncio.sleep(delay)
    return {"endpoint": endpoint, "data": f"data from {endpoint}"}


@app.get("/concurrent")
async def concurrent_fetch():
    """
    Fetch from multiple endpoints concurrently.
    Without concurrency: 3 + 2 + 1 = 6 seconds
    With concurrency: max(3, 2, 1) = 3 seconds
    """
    results = await asyncio.gather(
        fetch_data("service1", 3),
        fetch_data("service2", 2),
        fetch_data("service3", 1),
    )
    return {"results": results}


# ============================================================================
# 6. COMBINING ASYNC + BACKGROUND TASKS
# ============================================================================

class AgentTask(BaseModel):
    prompt: str
    model: str = "llama2"


async def run_agent(prompt: str, model: str, background_tasks: BackgroundTasks):
    """
    Simulate running an AI agent:
    1. Start immediately
    2. Return result
    3. Log in background
    """
    # Simulate agent execution
    await asyncio.sleep(1)
    result = f"Agent ({model}) response to: {prompt}"
    
    # Log in background
    background_tasks.add_task(log_task, task_id=1, action="agent run")
    
    return {"result": result}


@app.post("/agent")
async def run_agent_endpoint(task: AgentTask, background_tasks: BackgroundTasks):
    """
    Agent endpoint with streaming capability
    """
    result = await run_agent(task.prompt, task.model, background_tasks)
    return result


# ============================================================================
# 7. TIMEOUT PATTERN
# ============================================================================

async def long_running_operation():
    """Simulate a long operation"""
    await asyncio.sleep(10)
    return "done"


@app.get("/with-timeout")
async def endpoint_with_timeout():
    """Endpoint with timeout protection"""
    try:
        result = await asyncio.wait_for(
            long_running_operation(),
            timeout=2.0  # 2 second timeout
        )
        return {"result": result}
    except asyncio.TimeoutError:
        return {"error": "Operation timed out", "status": 408}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("async_patterns:app", host="0.0.0.0", port=8000, reload=True)
