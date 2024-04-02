# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    """
    Model representing a user profile.

    Fields:
    - user (OneToOneField): Reference to the associated user.
    - bio (TextField): User biography.
    - subscribed_to_newsletter (BooleanField): Whether the user is subscribed to the newsletter.
    """

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name="user_profile")
    bio = models.TextField(blank=True)
    subscribed_to_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

class NewsletterSubscriber(models.Model):
    """
    Model representing a newsletter subscriber.

    Fields:
    - email (EmailField): Subscriber's email address.
    - subscribed_at (DateTimeField): Date and time when the subscriber subscribed.
    """

    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
