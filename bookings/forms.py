# bookings/forms.py
# Simple booking form for the booking system
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    """
    Form for booking appointments.

    Allows users to select the date, start time, and end time for their appointment.

    Inherits from:
    - forms.ModelForm

    Attributes:
    - Meta: Contains information about the form's associated model (Booking) and the fields to include.
    """
    class Meta:
        model = Booking
        fields = ['date', 'start_time', 'end_time']

