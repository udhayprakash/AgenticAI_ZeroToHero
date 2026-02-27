# uv Quickstart Guide

Get started with uv in 2 minutes.

## Installation

### On Linux/macOS
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
uv --version
```

### On Windows (PowerShell)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version
```

## Creating a New Project

### Option 1: Initialize in Current Directory
```bash
mkdir my-agentic-app
cd my-agentic-app
uv init
```

### Option 2: Create New Directory
```bash
uv init my-agentic-app
cd my-agentic-app
```

## Project Structure

After `uv init`, your project looks like:

```
my-agentic-app/
├── .python-version      # Python version pinned to 3.11
├── pyproject.toml       # Project metadata and dependencies
├── README.md
└── src/
    └── my_agentic_app/
        └── __init__.py
```

## Adding Dependencies

### Add a Production Dependency
```bash
uv add fastapi
uv add langchain
uv add pydantic
```

### Add a Dev Dependency (testing, linting, etc.)
```bash
uv add --dev pytest
uv add --dev ruff
uv add --dev mypy
```

### Add Multiple at Once
```bash
uv add fastapi uvicorn langchain pydantic
uv add --dev pytest pytest-asyncio ruff
```

## Installing Dependencies

### Fresh Install
```bash
uv sync
```

This:
1. Creates a `.venv` automatically
2. Installs all dependencies
3. Creates/updates `uv.lock` file

### Adding Package to Existing Project
```bash
uv add requests
# This automatically:
# - Updates pyproject.toml
# - Updates uv.lock
# - Creates/updates .venv
```

## Running Code

### Run a Script
```bash
uv run main.py
```

### Run with Python
```bash
uv run python script.py
```

### Interactive Python Shell
```bash
uv run python
```

### No Need to Activate venv!
With uv, you **don't need** to activate the virtual environment manually.

**Old way (pip):**
```bash
source .venv/bin/activate
python script.py
deactivate
```

**Better way (uv):**
```bash
uv run python script.py  # Done!
```

## Understanding pyproject.toml

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-agentic-app"
version = "0.1.0"
description = "AI Agent Example"
requires-python = ">=3.11"

# Production dependencies
dependencies = [
    "fastapi>=0.104.0",
    "langchain>=0.1.0",
    "pydantic>=2.0.0",
]

# Optional dependencies
[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.2.0",
]

[tool.uv]
python-version = "3.11"
```

## Managing Versions

### Pin Exact Version
```bash
uv add 'langchain==0.1.5'
```

### Pin Minimum Version
```bash
uv add 'langchain>=0.1.0'
```

### Pin Range
```bash
uv add 'langchain>=0.1.0,<0.2.0'
```

### Update All Dependencies
```bash
uv lock --upgrade
uv sync
```

### Update Specific Package
```bash
uv add 'langchain==0.2.0'
```

## uv.lock File

This file is **automatically generated** and should be **committed to git**:

```bash
git add uv.lock
git commit -m "Lock dependencies"
```

Benefits:
- ✅ Reproducible installs across machines
- ✅ Exact version control
- ✅ Fast lockfile resolution

## Common Commands

```bash
# Initialize project
uv init [PATH]

# Add dependency
uv add PACKAGE
uv add --dev PACKAGE

# Sync all dependencies
uv sync

# Remove dependency
uv remove PACKAGE

# Run command in venv
uv run COMMAND

# Show installed packages
uv pip list

# Clean up unused packages
uv sync --clean

# Check for outdated packages
uv pip list --outdated
```

## Example: Setting Up a FastAPI Project

```bash
# 1. Create project
uv init fastapi-agent
cd fastapi-agent

# 2. Add dependencies
uv add fastapi uvicorn pydantic

# 3. Add dev dependencies
uv add --dev pytest pytest-asyncio

# 4. Create main.py
cat > src/fastapi_agent/main.py << 'EOF'
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, Agent!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
EOF

# 5. Run the server
uv run python -m uvicorn src.fastapi_agent.main:app --reload
```

## Troubleshooting

### Command not found: uv
Make sure the installation path is in your PATH:
```bash
source $HOME/.cargo/env
```

### Permission denied on installation
Try the manual install method or use `sudo`:
```bash
sudo curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Virtual environment not being used
Always use `uv run` or activate manually:
```bash
source .venv/bin/activate
python script.py
```

## Next Steps

- Read [FastAPI Basics](../0.3_fastapi_basics/)
- Check out [Testing & Quality](../0.4_testing_quality/)
