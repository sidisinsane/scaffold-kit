# Quick Setup Guide: Dynamic Versioning with Python

## Prerequisites

- Python 3.12 or later
- uv package manager
  ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- Git repository for your project

## Why Dynamic Versioning

**The Problem:** Traditional versioning requires manually keeping versions
synchronized across multiple files:

```python
# pyproject.toml
version = "1.2.3"
```

```python
# src/my_package/__init__.py
__version__ = "1.2.3"
```

```bash
# Git tag
git tag 1.2.3
```

This creates maintenance overhead and opportunities for human error.

**The Solution:** Use Git tags as your single source of truth. Everything else
derives the version automatically from your Git repository state.

## Setup: pyproject.toml Configuration

Configure your project to use VCS (Version Control System) versioning:

```toml
# pyproject.toml
[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"

[project]
name = "my-package"
description = "Your package description."
dynamic = ["version"]  # Version comes from Git tags
dependencies = []

[tool.hatch.version]
source = "vcs"
raw-options = { local_scheme = "no-local-version" }

# Optional: Generate version file during build
[tool.hatch.build.hooks.vcs]
version-file = "src/my_package/__version__.py"
template = '''
__version__ = "{version}"
'''
```

**Key points**:

- `requires = ["hatchling", "hatch-vcs"]` adds VCS versioning support to the
  build system
- `dynamic = ["version"]` tells the build system to determine version
  dynamically
- `source = "vcs"` means read from version control (Git tags)
- `raw-options = { local_scheme = "no-local-version" }` prevents messy dev
  versions like `1.2.3+g1234567`

**Git Tagging Convention**:

```bash
# Use semantic versioning
git tag 1.0.0    # Major release
git tag 1.1.0    # Minor release
git tag 1.1.1    # Patch release
```

## Accessing Versions in Code

### Simple Runtime Approach

```python
# src/my_package/__init__.py
from importlib import metadata

__version__ = metadata.version(__package__ or __name__)

__all__ = ["__version__"]
```

This works perfectly when your package is properly installed and leverages
Python's (3.12+) stable `importlib.metadata` API.

### With Development Fallback

If you need your code to work during development before installation:

```python
# src/my_package/__version__.py
__version__ = "dynamic"
```

```python
# src/my_package/__init__.py
try:
    from importlib import metadata
    __version__ = metadata.version(__package__ or __name__)
except Exception:
    # Fallback to build-generated version file
    try:
        from my_package.__version__ import __version__
    except ImportError:
        __version__ = "unknown"

__all__ = ["__version__"]
```

**When to use fallbacks:**

- Development workflows where you run code directly from source
- Testing scenarios before package installation
- You configured `version-file` in your `pyproject.toml`

## Workflow

### Development

```bash
# Clone and setup
git clone https://github.com/username/my-package.git
cd my-package
uv sync

# Check version works
uv run python -c "import my_package; print(my_package.__version__)"
# Output: 1.2.3 (from latest git tag)
```

### Building

```bash
# Build both source distribution (.tar.gz) and wheel (.whl)
uv build

# Output:
# dist/my_package-1.2.3.tar.gz            <- Source distribution
# dist/my_package-1.2.3-py3-none-any.whl  <- Wheel
```

Both distributions automatically get the version from your Git tags.

### Publishing

```bash
# Publish to PyPI (requires PyPI credentials configured)
# Export the variable first, then publish
export UV_PUBLISH_TOKEN=your_token_here
uv publish

# Or pass directly via command line
uv publish --token your_token_here
```

## Complete Working Example

### Project Structure

```asciidoc
my-package/
├── pyproject.toml
├── src/
│   └── my_package/
│       └── __init__.py
└── .git/
```

```toml
# pyproject.toml
[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"

[project]
name = "my-package"
description = "A sample package with dynamic versioning."
dynamic = ["version"]
dependencies = []

[tool.hatch.version]
source = "vcs"
```

```python
# src/my_package/__init__.py
from importlib import metadata

__version__ = metadata.version(__package__ or __name__)

def main():
    print(f"my-package version: {__version__}")

if __name__ == "__main__":
    main()
```

### Git Workflow

```bash
# Initial commit
git add .
git commit -m "Initial commit"

# Create your first release
git tag 0.1.0
git push origin main --tags

# Build and verify
uv build
uv run python -c "import my_package; print(my_package.__version__)"
# Output: 0.1.0
```

### Making a New Release

```bash
# Make changes, commit them
git add .
git commit -m "release: Add new feature xyz"

# Tag new version
git tag 0.2.0
git push origin main --tags

# Build automatically picks up new version
uv build
# Creates: my_package-0.2.0.tar.gz and my_package-0.2.0-py3-none-any.whl
```

## Key Benefits

- **Single source of truth:** Version exists only in Git tags
- **No manual synchronization:** Build system handles everything
- **Clean releases:** Tag and build - version is automatically correct
- **compatibility:** Works seamlessly with modern Python tooling
- **Standard compliance:** Uses Python 3.12+ stable APIs

## Next Steps

Once you have dynamic versioning working, consider these enhancements:

### Automated Releases

- Set up Semantic Release with conventional commits for automatic version
  bumping
- Add GitHub Actions to automatically publish to PyPI when you push tags

### Development Enhancements

- Configure pre-commit hooks to validate version consistency
- Handle development versions for dirty working directories or unreleased
  commits

### Advanced Configuration

- Customize version file templates and generate multiple output formats
- Adapt configuration for monorepos or complex project structures

### Integration Improvements

- Auto-inject versions into documentation builds
- Align Docker image tags with package versions
- Generate release notes automatically from commit history
