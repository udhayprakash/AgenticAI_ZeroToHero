# FastAPI Basics for Agent Serving

Learn to build production REST APIs that serve your AI agents.

## Topics Covered

1. **Why FastAPI for Agents**
   - Async/await for concurrent agent execution
   - Built-in API documentation
   - Fast performance (second only to bare ASGI)
   - Type hints with Pydantic

2. **Core FastAPI Concepts**
   - Application setup
   - Routes (GET, POST, etc.)
   - Request/Response models with Pydantic
   - Async functions

3. **Serving LangGraph Agents**
   - Exposing agent endpoints
   - Streaming responses
   - Error handling

4. **Deployment Considerations**
   - Running with uvicorn
   - Docker containerization
   - Health checks

## Files in This Section

- `basic_app.py` - Minimal FastAPI application
- `with_pydantic_models.py` - Request/response models
- `agent_endpoint.py` - Example agent serving endpoint
- `async_patterns.py` - Common async patterns

## Key Learning Objectives

- [ ] Create a basic FastAPI application
- [ ] Define request and response models
- [ ] Write async route handlers
- [ ] Test API endpoints
- [ ] Understand async/await for agents
