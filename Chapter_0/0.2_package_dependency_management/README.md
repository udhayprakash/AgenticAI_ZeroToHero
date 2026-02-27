# 0.2 Package & Dependency Management

Master modern Python package management in 2026: comparing pip, Poetry, and uv.

## Topics Covered

1. **Traditional pip + venv**
   - When to use pip (legacy projects, simple scripts)
   - Virtual environment setup
   - Requirements management

2. **Poetry**
   - Strengths for library publishing
   - Dependency resolution
   - Why it's slower than alternatives

3. **uv (Astral) – The 2026 Standard**
   - 10–100× faster installs and dependency resolution
   - Replaces pip, poetry, pyenv, and pipx
   - pyproject.toml + uv.lock workflow
   - Automatic virtual environment management
   - uv add / uv sync commands

4. **Practical Migration**
   - Converting from pip to uv
   - Converting from Poetry to uv
   - Managing monorepos with uv

## Files in This Section

- `pip_vs_poetry_vs_uv.md` - Detailed comparison
- `uv_quickstart.md` - Getting started with uv
- `examples/` - Example projects with different package managers
  - `pip_project/` - Traditional pip setup
  - `poetry_project/` - Poetry setup
  - `uv_project/` - Modern uv setup

## Key Learning Objectives

- [ ] Understand pros and cons of each package manager
- [ ] Set up a project with uv
- [ ] Migrate an existing project from pip or Poetry to uv
- [ ] Use uv for dependency management and version pins
- [ ] Understand pyproject.toml format
