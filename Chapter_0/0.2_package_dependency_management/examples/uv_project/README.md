# UV Project Example

Modern UV setup - the 2026 standard!

## Structure

```
uv_project/
├── .python-version      # Python version (3.11)
├── pyproject.toml       # Project metadata and dependencies
├── uv.lock              # Lock file for reproducible installs
├── README.md
├── src/
│   └── app.py
└── tests/
    └── test_app.py
```

## Setup

```bash
# Install UV (one time)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create new project
uv init my-project
cd my-project

# Add dependencies
uv add requests fastapi pydantic

# Add dev dependencies
uv add --dev pytest ruff

# Install all dependencies
uv sync

# Run commands (no activation needed!)
uv run python src/app.py
uv run pytest
```

## pyproject.toml

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "uv-example"
version = "0.1.0"
description = "Example UV project"
requires-python = ">=3.11"

dependencies = [
    "requests>=2.28.0",
    "pydantic>=2.0.0",
    "fastapi>=0.104.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.2.0",
]

[tool.uv]
python-version = "3.11"
```

## Key Commands

### Project Management
- `uv init` - Create new project
- `uv sync` - Install dependencies
- `uv lock` - Update lock file

### Adding Packages
- `uv add requests` - Add production dependency
- `uv add --dev pytest` - Add dev dependency

### Running
- `uv run python script.py` - Run script
- `uv run pytest` - Run tests (automatic venv!)

## Pros
- ✅ 10-100× faster than pip/Poetry
- ✅ Single tool: replaces pip, poetry, pyenv, pipx
- ✅ Lock file for reproducibility
- ✅ No activation needed
- ✅ Automatic venv management
- ✅ Modern standard in 2026

## Cons
- ❌ Still relatively new
- ❌ Smaller ecosystem than pip
- ❌ Some edge cases may not be covered

## Migration from pip

```bash
# Old pip project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# New UV way
uv sync  # That's it!
```

## Migration from Poetry

Just use `uv sync` - it reads poetry.lock and pyproject.toml!
