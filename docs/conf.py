# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime
from setuptools.config import read_configuration


# -- Path setup --------------------------------------------------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------------------------------------------------

conf = read_configuration("../setup.cfg")

author = conf["metadata"]["author"]
copyright = f"{datetime.now().year}, {author}"
project = conf["metadata"]["name"]
release = conf["metadata"]["version"]
version = release


# -- General configuration ---------------------------------------------------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "*.egg-info",
    ".coverage",
    ".DS_Store",
    ".gitignore",
    ".tox",
    "build",
    "data",
    "dist",
    "htmlcov",
    "MANIFEST.in",
    "tests",
    "Thumbs.db",
    "tox.ini",
]


# -- Options for HTML output -------------------------------------------------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"


# -- sphinx.ext.napoleon -------------------------------------------------------------------------------------------

napoleon_google_docstring = True
