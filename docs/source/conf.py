# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python-Curriculum'
copyright = '2024, The League'
author = 'The League'

html_title = 'Python'
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



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo' # 'alabaster'
html_static_path = ['_static']
