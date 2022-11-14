# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
from pathlib import Path

_DOCS_PATH = Path(__file__).parent
_ROOT_PATH = _DOCS_PATH.parent

sys.path.insert(0, str(_ROOT_PATH))
from ooodev import __version__

os.environ["DOCS_BUILDING"] = "True"
os.environ["ooouno_ignore_runtime"] = "True"

# -- Project information -----------------------------------------------------

project = "ODEV GUI Automation for windows"
copyright = "2022, :Barry-Thomas-Paul: Moss"
author = ":Barry-Thomas-Paul: Moss"
release = "0.3.0"

odev_url = "https://python-ooo-dev-tools.readthedocs.io/en/latest/"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx_rtd_dark_mode",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_toolbox.collapse",
    "sphinx_toolbox.more_autodoc.autonamedtuple",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_tabs.tabs",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

html_css_files = []
html_css_files = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"]
html_css_files.append("css/readthedocs_custom.css")
if html_theme == "sphinx_rtd_theme":
    html_css_files.append("css/readthedocs_dark.css")

html_js_files = [
    "js/custom.js",
]

# Napoleon settings
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
napoleon_google_docstring = True
napoleon_include_init_with_doc = True

autodoc_mock_imports = ["uno", "unohelper", "com"]

rst_prolog = """.. |odev_tools| replace:: OOO Development Tools
.. _odev_tools: https://python-ooo-dev-tools.readthedocs.io/en/latest/index.html

.. |impress_make_slides| replace:: Impress Make Slides
.. _impress_make_slides: https://github.com/Amourspirit/python-ooouno-ex/tree/main/ex/auto/impress/odev_make_slides

.. |impress_append_slides| replace:: Impress append Slides to existing slide show
.. _impress_append_slides: https://github.com/Amourspirit/python-ooouno-ex/tree/main/ex/auto/impress/odev_append_slides

.. |odev_part3| replace:: OOO Development Tools - Part 3: Draw & Impress
.. _odev_part3: https://python-ooo-dev-tools.readthedocs.io/en/latest/odev/part3/index.html
"""

rst_prolog += f".. |app_name| replace:: {project}"

# set if figures can be referenced as numers. Defalut is False
numfig = True

# set is todo's will show up.
# a master list of todo's will be on bottom of main page.
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#module-sphinx.ext.todo
todo_include_todos = False

# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_mock_imports
autodoc_mock_imports = []

autodoc_mock_imports.append("pywinauto")
autodoc_mock_imports.append("com")
autodoc_mock_imports.append("uno")

# region intersphinx
intersphinx_mapping = {"odev": (odev_url, None)}

# endregion intersphinx
