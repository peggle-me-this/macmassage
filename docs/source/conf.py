# Configuration file for the Sphinx documentation builder.

import os
print("DJANGO_SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))
import sys
print("Python Path:", sys.path)
import django
# Import Django settings
from django.conf import settings
from dotenv import load_dotenv

# Add the parent directory of your Django project to sys.path
sys.path.insert(0, os.path.abspath('..'))

# Load environment variables from the .env file
load_dotenv()

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'macmassage_site.settings'


# If necessary, call django.setup()
#django.setup()

# Read requirements.txt and install dependencies
requirements_path = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')
if os.path.exists(requirements_path):
    with open(requirements_path) as f:
        requirements = f.read().splitlines()
        for requirement in requirements:
            os.system(f'pip install {requirement}')
            
# -- Project information -----------------------------------------------------
project = 'Macmassage Website'
copyright = '2024, Bronwyn Barnes'
author = 'Bronwyn Barnes'
release = '1.3'

# -- General configuration ---------------------------------------------------
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
