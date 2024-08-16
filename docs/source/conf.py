# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python-Apprentice'
copyright = '2024, The League'
author = 'Eric Busboom'

html_title = 'Python Apprentice'
html_logo = 'https://images.jointheleague.org/logos/logo4.png'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    'myst_parser',
    'sphinx_togglebutton',
    'sphinx_design'
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "colon_fence"
]

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = []

html_last_updated_fmt = '%b %d, %Y %H:%M'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo' # 'alabaster'
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

html_extra_path = ['html']
