# Poetry Project Example

Modern Poetry setup with better dependency management.

## Structure

```
poetry_project/
├── .python-version          # Python version (3.11)
├── pyproject.toml           # Project metadata and dependencies
├── poetry.lock              # Lock file for reproducible installs
├── README.md
├── src/
│   └── app.py
└── tests/
    └── test_app.py
```

## Setup

```bash
# Install Poetry (one time)
curl -sSL https://install.python-poetry.org | python3 -

# Create new project
poetry new my-project
cd my-project

# Or initialize in existing directory
poetry init

# Add dependencies
poetry add requests fastapi pydantic

# Add dev dependencies
poetry add --group dev pytest ruff black

# Install all dependencies
poetry install

# Run commands
poetry run python src/app.py
poetry run pytest
```

## pyproject.toml

```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""

[tool.poetry.dependencies]
python = "^3.11"
requests = "^2.28.0"
fastapi = "^0.104.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
ruff = "^0.2.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## Pros
- ✅ Lock file for reproducibility
- ✅ Better for publishing libraries
- ✅ Built-in dev dependencies
- ✅ Good documentation
- ✅ Single command for install

## Cons
- ❌ Slower than uv (30-60 seconds)
- ❌ More resource-heavy
- ❌ Learning curve for Poetry CLI
- ❌ Heavier installation
