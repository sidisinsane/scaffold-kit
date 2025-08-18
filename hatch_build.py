# pylint: disable=broad-except,import-error,import-outside-toplevel,unused-variable,too-many-locals
"""Hatchling build hook for scaffold-kit.

This build hook automatically generates a package __init__.py
from metadata in pyproject.toml during the build process.
"""

from __future__ import annotations

import sys

from pathlib import Path
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    """Custom build hook to generate __init__.py from pyproject.toml."""

    PLUGIN_NAME = "custom"
    PACKAGE_PATH = "src/scaffold_kit"

    def initialize(self, version: str, _build_data: dict[str, Any]) -> None:
        """Initialize the build hook and generate __init__.py.

        Args:
            version: The version being built
            _build_data: Build configuration data (unused)
        """
        self.app.display_info("Generating __init__.py from pyproject.toml...")

        # Import tomllib (Python 3.11+) or fallback to tomli.
        try:
            if sys.version_info >= (3, 11):
                import tomllib
            else:
                try:
                    import tomli as tomllib
                except ImportError as e:
                    self.app.abort(
                        "tomli is required for Python < 3.11. "
                        "Install it with: pip install tomli"
                    )
        except Exception as e:
            self.app.abort(f"Failed to import TOML library: {e}")

        # Read pyproject.toml
        pyproject_path = Path(self.root) / "pyproject.toml"
        if not pyproject_path.exists():
            self.app.abort(f"pyproject.toml not found at {pyproject_path}")

        try:
            with open(pyproject_path, "rb") as f:
                pyproject = tomllib.load(f)
        except Exception as e:
            self.app.abort(f"Failed to parse pyproject.toml: {e}")

        # Extract pyproject metadata.
        metadata = pyproject.get("project", {})
        if not metadata:
            self.app.abort("No [project] section found in pyproject.toml")

        # Get required fields with validation.
        meta_name = metadata.get("name")
        if not meta_name:
            self.app.abort("Project name not found in pyproject.toml")

        # Get optional fields and set defaults.
        meta_description = metadata.get("description", "")
        meta_authors = metadata.get("authors", [])

        meta_author = ""
        meta_email = ""
        if meta_authors:
            first_author = meta_authors[0]
            meta_author = first_author.get("name", "")
            meta_email = first_author.get("email", "")

        meta_urls = metadata.get("urls", {})
        meta_url = meta_urls.get("Homepage", "")

        # Generate __init__.py content.
        init_content = f'''"""Scaffold-kit package initialization.

This file is auto-generated from pyproject.toml during the build process.
Do not edit manually - your changes will be overwritten!

This package provides utilities for scaffolding projects from structured data,
with complementary tools for generating file checklists and rendering ASCII
trees.
"""

from __future__ import annotations


__version__ = "{version}"
__author__ = "{meta_author}"
__email__ = "{meta_email}"
__title__ = "{meta_name}"
__description__ = "{meta_description}"  # noqa: E501
__url__ = "{meta_url}"

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__title__",
    "__description__",
    "__url__",
]
'''

        # Set path to package __init__.py.
        init_path = Path(self.root) / self.PACKAGE_PATH / "__init__.py"

        # Ensure the directory exists.
        init_path.parent.mkdir(parents=True, exist_ok=True)

        # Write to package __init__.py.
        try:
            init_path.write_text(init_content, encoding="utf-8")
            self.app.display_info(f"Generated {init_path}")
        except Exception as e:
            self.app.abort(f"Failed to write {init_path}: {e}")
