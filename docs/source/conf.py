# -*- coding: utf-8 -*-
"""
Configuration file for the Sphinx documentation builder.
"""
__author__ = "Anders Åström"
__contact__ = "anders@lyngon.com"
__copyright__ = "2022, Lyngon Pte. Ltd."
__license__ = """(c) Copyright 2022 Lyngon Pte. Ltd., All rights reserved."""

# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import configparser

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from typing import Dict, List

from packaging.version import Version

config_file = "../../setup.cfg"
config = configparser.ConfigParser()
config.read(config_file)
current_version = Version(config.get("metadata", "version", fallback="0.0.0"))

sys.path.insert(0, os.path.abspath("../../src/"))

on_rtd = os.environ.get("READTHEDOCS") == "True"

# -- Project information -----------------------------------------------------

project = config.get("metadata", "description", fallback="Python Project")
copyright = "2022, Lyngon Pte. Ltd."
author = config.get("metadata", "author", fallback="Anonymous")
version = str(current_version)


# -- General configuration ---------------------------------------------------
autoclass_content = "both"
autodoc_member_order = "bysource"

autodoc_type_aliases: Dict[str, str] = {}

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions: List[str] = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_tabs.tabs",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: List[str] = []


# -- Options for HTML output -------------------------------------------------

# pygments_style = "fruity"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    # "analytics_anonymize_ip": True,
    "display_version": True,
    "prev_next_buttons_location": "both",
    "style_external_links": True,
    # "style_nav_header_background": "#7a0c00",
}

html_logo = "../images/LyngonLogo_v3_trimmed.png"
html_favicon = "../images/LyngonIcon_v3.ico"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# custom.css is inside one of the html_static_path folders (e.g. _static)
html_css_files = ["custom.css"]

ml_css_files = []  # type: List[str]
