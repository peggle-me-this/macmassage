# newsletters/admin.py

from django.contrib import admin
from .models import Newsletter

admin.site.register(Newsletter)
"""
Admin configuration for the Newsletter model.
"""