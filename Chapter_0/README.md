# Chapter 0: Foundations – Python & Tooling Setup for Agentic Development

**Goal:** Establish a fast, modern, reproducible development environment without legacy friction.

## Overview

This chapter covers the essential setup and foundational tools needed to start building agentic AI applications. We'll configure a production-ready development environment and learn the modern Python tooling stack for 2026.

## Sections

### [0.1 Python Dev Setup](./0.1_python_dev_setup/README.md)
- GitHub Codespaces + devcontainer.json configuration
- VS Code extensions setup
- Docker fundamentals for MCP servers

### [0.2 Package & Dependency Management](./0.2_package_dependency_management/README.md)
- pip, Poetry, and uv comparison
- Why uv is the modern choice
- Hands-on migration from pip to uv

### [0.3 FastAPI Basics for Agent Serving](./0.3_fastapi_basics/README.md)
- Setting up a FastAPI application
- Pydantic models for structured data
- Building async routes for agents

### [0.4 Testing & Quality Essentials](./0.4_testing_quality/README.md)
- Unit testing with pytest
- Mocking LLM calls and tools
- Property-based testing
- Load testing with Locust

## Duration
1–2 sessions (theory + hands-on setup)

## Key Takeaways
By the end of this chapter, you should be able to:
- Set up a reproducible development environment
- Manage Python dependencies efficiently using uv
- Create a simple FastAPI server
- Write and execute tests for your code

## Prerequisites
- Basic programming experience
- Familiarity with command line and Git (recommended)
