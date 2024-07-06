# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from os.path import abspath, dirname, join

import django
import tomllib

import backend

_ = dir(backend)
os.environ["DJANGO_SETTINGS_MODULE"] = "statracking.settings"
os.environ["DJANGO_NINJA_SECRET_KEY"] = "something"

cwd = dirname(abspath(__file__))
root = join(cwd, "../..")

sys.path.insert(0, root)
django.setup()


toml_file = join(root, "pyproject.toml")

with open(toml_file, "rb") as f:
    data = tomllib.load(f)
    tool = data.get("tool")
    if not isinstance(tool, dict):
        raise ValueError("Check your pyproject.toml file")

    version = tool["poetry"]["version"]


release = version

project = "Python Template"
copyright = "2023, Masum Billal"
author = "Masum Billal"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "LICENSE", ".tox", "*env/", ".venv"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"

html_theme_options: dict[str, str] = {}
html_context = {"default_mode": "dark"}

html_static_path: list[str] = []
