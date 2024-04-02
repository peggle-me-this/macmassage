# urls.py
from django.urls import path
from .views import send_newsletter

urlpatterns = [
    path('send-newsletter/', send_newsletter, name='send_newsletter'),
    # Other URL patterns
]