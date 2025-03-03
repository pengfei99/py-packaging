# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
extensions = [
    "sphinx.ext.autodoc",         # Generates docs from docstrings
    "sphinx.ext.napoleon",        # Supports Google and NumPy style docstrings
    "sphinx.ext.viewcode",        # Adds source code links
    "sphinx_autodoc_typehints",   # Adds type hints in docs
]

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'StockCatcher'
copyright = '2025, pengfei liu'
author = 'pengfei liu'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []


import os
import sys
sys.path.insert(0, os.path.abspath("/home/pliu/git/py-packaging"))  # Adjust path to include project root


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

autodoc_mock_imports = ["pandas", "numpy"]  # Prevents errors for missing dependencies