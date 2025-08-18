# scaffold-kit

A utility for scaffolding projects from structured data, with complementary
tools for generating file checklists and rendering ASCII trees.

## Project Overview

This tool streamlines project setup and documentation through a simple
three-step workflow:

1. **Scaffold**: Create complete project structures from YAML or JSON
   definitions
2. **Track**: Generate checklists to monitor which files need content
3. **Document**: Create ASCII tree diagrams for documentation and visualization

The tool works out of the box with sensible defaults but is easily customizable
via configuration files.

**Key Features:**

- Creates nested folder structures with empty files from simple YAML/JSON
  definitions
- Generates interactive checklists showing which files are empty vs. populated
- Produces ASCII tree diagrams for documentation (full project or partial views)
- Respects ignore patterns (`.gitignore` style) for clean output
- Fully configurable through `.scaffoldkitrc` files

## Getting Started

### Installation

Install using your preferred Python package manager:

```bash
# Using pip (comming soon)
pip install scaffold-kit

# Using uv
uv add scaffold-kit

# Development installation
git clone https://github.com/sidisinsane/scaffold-kit.git
cd scaffold-kit
uv sync --all-extras
```

### Quick Start

1. **Create a scaffold definition file** (`scaffold.yaml`):

> **Important**: Place this file in the target directory where you want the
> structure created, or in the parent directory if using the `--root` flag.

```yaml
name: my-project
type: folder
children:
  - name: src
    type: folder
    children:
      - name: my_project
        type: folder
        children:
          - name: __init__.py
            type: file
          - name: main.py
            type: file
  - name: tests
    type: folder
    children:
      - name: test_main.py
        type: file
  - name: README.md
    type: file
  - name: pyproject.toml
    type: file
```

2. **Scaffold your project structure**:

```bash
# Create structure in current directory
scaffold-kit scaffold

# Create root folder and structure
scaffold-kit scaffold --root
```

3. **Track your progress with a checklist**:

```bash
scaffold-kit checklist
```

This generates `empty-files-checklist.txt`:

```text
[ ] src/my_project/__init__.py
[ ] src/my_project/main.py
[ ] tests/test_main.py
[ ] README.md
[x] pyproject.toml
```

4. **Generate documentation trees**:

```bash
# Full project tree
scaffold-kit tree

# Partial tree for specific directory
scaffold-kit tree src/
```

### Configuration

Customize behavior by creating a `.scaffoldkitrc.yaml` file in your project
root:

```yaml
scaffold_file: scaffold.yaml
ignore_file: .scaffoldkitignore
checklist_directory: .
checklist_file: empty-files-checklist.txt
tree_file: tree.txt
tree_directory: .
```

> **Note**: Configuration and ignore files must be placed in the root directory
> where you'll run the commands. You can copy these files directly from the
> `examples/configs/` directory.

**Configuration file search order:**

1. `.scaffoldkitrc.yaml`
2. `scaffoldkitrc.yaml`
3. `.scaffoldkitrc`
4. `.scaffoldkitrc.json`
5. `scaffoldkitrc.json`

### Command Reference

#### scaffold

Creates project structure from YAML or JSON definition.

```bash
scaffold-kit scaffold [--root]
```

- `--root, -r`: Create the root folder defined in the scaffold file

#### checklist

Generates a checklist of files marking empty `[ ]` vs. populated `[x]` files.

```bash
scaffold-kit checklist
```

#### tree

Creates ASCII tree representation of directory structure.

```bash
scaffold-kit tree [directory] [--ignore-file FILE]
```

- `directory`: Target directory (default: current directory)
- `--ignore-file`: Custom ignore file (default: `.scaffoldkitignore`)

## Navigation Aid

### Project Structure

- **`examples/`**: Sample scaffold definitions and configuration files
  - `examples/scaffold/`: Example YAML and JSON scaffold definitions
  - `examples/configs/`: Various configuration file examples and formats
  - `examples/.scaffoldignore`: Ignore file
- **`src/scaffold_kit/`**: Main source code
- **`tests/`**: Test suite
- **Configuration files**: `.scaffoldkitrc.yaml`, `.scaffoldignore` for
  customizing behavior

### Key Files

- **`scaffold.yaml`** (or custom): Defines your project structure
- **`.scaffoldkitrc.yaml`**: Customizes tool behavior and file names
- **`.scaffoldkitignore`**: Patterns to exclude from tree and checklist
  generation

### Documentation

- **Homepage**:
  [https://github.com/sidisinsane/scaffold-kit](https://github.com/sidisinsane/scaffold-kit)
- **Documentation**:
  [https://sidisinsane.github.io/scaffold-kit](https://sidisinsane.github.io/scaffold-kit)
- **Examples**: Browse the `examples/` directory for scaffold templates and
  configuration options
