# macmassage_site/celery.py
# Not currently in use 
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'macmassage_site.settings')

# Create a Celery instance
app = Celery('macmassage_site')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in all apps included in INSTALLED_APPS
app.autodiscover_tasks()


