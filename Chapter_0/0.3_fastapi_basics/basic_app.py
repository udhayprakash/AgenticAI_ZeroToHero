#!/usr/bin/env python3
"""
Minimal FastAPI Application

Run with:
    uv run python basic_app.py
    # or
    uv run uvicorn basic_app:app --reload

Then visit: http://localhost:8000/docs
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create FastAPI app
app = FastAPI(
    title="Basic Agent API",
    description="A minimal FastAPI application",
    version="0.1.0"
)


@app.get("/")
async def read_root():
    """Root endpoint"""
    return {"message": "Welcome to AgenticAI!"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/items/{item_id}")
async def get_item(item_id: int, query: str = None):
    """
    Get an item by ID
    
    - **item_id**: Item identifier (path parameter)
    - **query**: Optional query parameter
    """
    return {
        "item_id": item_id,
        "query": query
    }


@app.post("/echo")
async def echo(message: str):
    """Echo back a message"""
    return {"echo": message}


if __name__ == "__main__":
    import uvicorn
    
    # Run server
    uvicorn.run(
        "basic_app:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # Auto-reload on file changes
    )
