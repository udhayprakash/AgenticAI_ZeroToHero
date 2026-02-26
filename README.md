# AgenticAI_ZeroToHero – Revised Course Outline (2026 Edition)

**Theme:** The "Zero-Cost" Professional Stack for Autonomous, Reliable Agentic AI

**Focus:** Local-first development, MCP standardization, LangGraph reliability, production-grade practices

**Target Audience:** Developers moving from zero to production-hero level in agentic AI

**Prerequisites:** Basic programming experience; familiarity with command line and Git recommended

---

## Chapter 0: Foundations – Python & Tooling Setup for Agentic Development

**Goal:** Establish a fast, modern, reproducible development environment without legacy friction.

### 0.1 Python Dev Setup
- GitHub Codespaces + devcontainer.json (pre-configured uv, Ollama, FastAPI)
- VS Code extensions: Ruff, Continue.dev, Docker
- Docker basics: When to containerize MCP servers or agents

### 0.2 Package & Dependency Management in 2026
- **Traditional pip + venv:** When it's still useful (simple scripts, legacy)
- **Poetry:** Strengths for library publishing, but slower resolution
- **uv (Astral):** The 2026 default – 10–100× faster installs/resolution, replaces pip/poetry/pyenv/pipx, pyproject.toml + uv.lock, automatic venvs, uv add / uv sync workflow
- **Hands-on:** Migrate a small project from pip → uv

### 0.3 FastAPI Basics for Agent Serving
- Why FastAPI → production REST/async endpoints for LangGraph agents
- Quick setup: Basic app, Pydantic models, async routes, /docs (Swagger UI)

### 0.4 Testing & Quality Essentials
- **unittest / pytest:** Unit tests for tools, nodes, Pydantic schemas
- **Mocking:** LLM calls & tools (unittest.mock, LangChain test utilities)
- **Property-based testing:** For structured outputs
- **Locust:** Basic load testing of FastAPI endpoints


**Duration:** 1–2 sessions (theory + hands-on setup)

---

## Chapter 1: The Engine Room (Setup & Local LLMs)

**Goal:** Build a high-performance development environment without a credit card.

### 1.1 The 2026 Workflow
Why we moved from Python pip to uv for blazing-fast dependency management

### 1.2 Ollama Mastery
Running local models (Llama 3.3 8B, Mistral Nemo) to handle logic without API latency or costs

### 1.3 OpenRouter & LiteLLM
Configuring a "Cloud Failover" using OpenRouter's free tier models (Gemini 2.0 Flash) for high-reasoning tasks

### 1.4 Environment Parity
Setting up GitHub Codespaces with custom devcontainer for identical execution across environments

---

## Chapter 2: The Logic Layer (LangChain & LangFlow)

**Goal:** Master the fundamental building blocks of AI reasoning.

### 2.1 LCEL (LangChain Expression Language)
Writing declarative, readable code that bridges prompts and models

### 2.2 Structured Outputs
Using Pydantic to force LLMs to speak in strict JSON—the "API-fication" of thought

### 2.3 Tool Calling
Giving agents "hands" using the DuckDuckGo Search tool (no API key needed)

### 2.4 Visual Prototyping with LangFlow
Rapidly testing agent logic on a visual canvas before committing to code

---

## Chapter 3: The Universal Adapter (MCP - Model Context Protocol)

**Goal:** Standardize how agents interact with your data and tools.

### 3.1 The MCP Revolution
Understanding why we stopped writing custom "tools" and started building MCP Servers

### 3.2 FastMCP SDK
Building a local Python-based MCP server (filesystem access, SQLite queries)

### 3.3 Security Best Practices
- Least-privilege (read-only tools)
- Sandboxing (Docker/container limits)
- Auth scopes and audit logging

### 3.4 The Bridge
Connecting your MCP server to LangChain/LangGraph using the langchain-mcp adapter

### 3.5 Interoperability
Using the same MCP tool across Claude Desktop, local agents, and enterprise apps

---

## Chapter 4: The Nervous System (LangGraph & State)

**Goal:** Build complex, non-linear workflows that can loop and self-correct.

### 4.1 Cycles over Chains
Why the AgentExecutor is dead and why LangGraph is the future

### 4.2 State Management
Defining a global State object that flows through nodes (TypedDict / Pydantic)

### 4.3 Self-Correction Pattern
Building a "Reflection Node" where an agent critiques its own work and loops until it passes

### 4.4 Error Handling & Resilience
- Multi-level (node/graph/app)
- Bounded retries + exponential backoff
- Fallback nodes (e.g., switch model on timeout)
- Graceful degradation

### 4.5 Persistence & Time Travel
Using Checkpointers to save agent state and revert on failure

---

## Chapter 5: Multi-Agent Orchestration

**Goal:** Scaling from a solo agent to a collaborative "Digital Workforce."

### 5.1 The Supervisor Pattern
Building a "Manager" agent that delegates work to specialized "Researcher" and "Writer" nodes

### 5.2 The Handoff Pattern
Direct agent-to-agent communication for high-speed workflows

### 5.3 Human-in-the-Loop (HITL)
Adding "Breakpoints" to your graph for approval-based workflows

---

## Chapter 6: Observability, Testing & Production

**Goal:** Move from a "toy" to a reliable, monitored production system.

### 6.1 LangSmith Tracing
Inspecting the "black box"—seeing exactly what prompts and tool calls occurred

### 6.2 Evaluation Sets
Building "Golden Datasets" to test if a model upgrade breaks your agent's logic

### 6.3 LLM-as-a-Judge
Using free models to automatically grade production agent performance

### 6.4 Advanced Testing
- Graph-level integration tests
- Mock tools/state
- Property-based checks
- CI/CD integration (pytest + GitHub Actions)

### 6.5 Deployment
Turning your graph into a scalable REST API (LangGraph Cloud or FastAPI). Locust load testing demo.

---

## Chapter 7: Memory, RAG & Scaling Patterns (Bonus – Recommended Extension)

**Goal:** Add long-term context and handle real-world scale.

### 7.1 Simple RAG via MCP
Vector store (Chroma/Qdrant) exposed as MCP server

### 7.2 Long-term Memory Patterns
Conversation summary + vector retrieval

### 7.3 Caching & Parallelism
Redis for repeated calls, async node execution

### 7.4 When to Go Paid
Rate-limit handling, cost monitoring, hybrid local ↔ frontier model routing

---

## Capstone Project: Autonomous Research & Report Agent

**The Mission:** Build an end-to-end agentic system that:

- Receives a complex query (e.g., "Analyze the 2026 semiconductor market")
- Uses an MCP Server to check local files for existing data
- Uses DuckDuckGo to fill research gaps
- Self-reflects & corrects with bounded retries
- Produces a structured Markdown report
- Includes basic observability (LangSmith traces) and unit tests

**Cost:** $0.00 total execution cost

**Bonus Challenges:**
- Add HITL approval before final report
- Expose via FastAPI endpoint
- Run Locust load test