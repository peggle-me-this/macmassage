# newsletter/models.py
from django.db import models
from django.contrib.auth.models import User

class Newsletter(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    recipients = models.ManyToManyField(User)
"""
Model representing a newsletter, with a subject, message, and recipients.
"""
    
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
"""
Model representing a subscriber to the newsletter.
"""