# forms.py
from django import forms
from .models import Newsletter

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'message', 'recipients']
"""
Form for creating and updating newsletters.
"""