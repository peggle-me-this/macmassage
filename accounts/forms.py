# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User

class ProfileEditForm(forms.ModelForm):
    """
    Form for editing user profile.

    Fields:
    - bio (TextField): User biography.
    - subscribed_to_newsletter (BooleanField): Whether the user is subscribed to the newsletter.
    """

    class Meta:
        model = UserProfile
        fields = ['bio', 'subscribed_to_newsletter']

class LoginForm(forms.Form):
    """
    Form for user login.

    Fields:
    - username (CharField): User's username.
    - password (CharField): User's password.
    """

    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
class RegisterForm(UserCreationForm):
    """
    Form for user registration.

    Fields:
    - username (CharField): User's username.
    - email (EmailField): User's email.
    - password1 (CharField): User's password.
    - password2 (CharField): Confirmation of user's password.
    """

    class Meta:
        model=User
        fields = ['username','email','password1','password2']
