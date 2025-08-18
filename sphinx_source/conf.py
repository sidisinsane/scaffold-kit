# pylint: disable=redefined-builtin
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from __future__ import annotations

import os
import sys


# Path to the project root: one level up from sphinx-source, then into src
HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(HERE, "../src"))

project = "Scaffold Kit"
copyright = "2025, Dirk Sidney Jansen"
author = "Dirk Sidney Jansen"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Google-style docstrings
    "sphinx.ext.viewcode",
    "sphinx_favicon",
    "myst_parser",  # Markdown parser
]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# Markdown parser settings
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]
html_theme = "alabaster"  # Default theme
html_title = "Scaffold Kit"  # (Optional) Overridden by `html_logo`
html_logo = (
    "_static/logo.svg"  # (Optional) Place in `sphinx_source/_static/logo.svg`
)

# -- Option for favicons -------------------------------------------------------
favicons = [
    {"rel": "shortcut icon", "sizes": "any", "href": "favicon.ico"},
]
