# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Macmassage Website'
copyright = '2024, Bronwyn Barnes'
author = 'Bronwyn Barnes'
release = '1.3'# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

sys.path.insert(0, os.path.abspath('..'))
# Set the Django settings module environment variable for the specific app
os.environ['DJANGO_SETTINGS_MODULE'] = 'about_macmassage.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'accounts.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'bookings.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'macmassage_site.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'newsletter.settings'

#django.setup()

project = 'Macmassage Website'
copyright = '2024, Bronwyn Barnes'
author = 'Bronwyn Barnes'
release = '1.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Google-style docstrings
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]


templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

