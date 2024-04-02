# about_mamassage/apps.py
from django.apps import AppConfig


class AboutMacmassageConfig(AppConfig):
    """
    AppConfig class for the 'about_macmassage' app.

    Attributes:
    - default_auto_field (str): The default auto field for the app's models.
    - name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about_macmassage'