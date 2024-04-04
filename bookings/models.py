# bookings/models.py
# Booking models for the booking app allowing the use of booking, appointment, special events and trading hours
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Booking(models.Model):
    """
    Model for booking appointments.

    Represents an appointment booking with date, start time, end time, user, status, notes, price,
    and payment status.

    Inherits from:
    - models.Model

    Attributes:
    - STATUS_CHOICES (list): Choices for booking status.
    - user_profile (ForeignKey): Reference to the user profile associated with the booking.
    - date (DateField): Date of the booking.
    - start_time (TimeField): Start time of the booking.
    - end_time (TimeField): End time of the booking.
    - status (CharField): Status of the booking.
    - notes (TextField): Additional notes for the booking.
    - price (DecimalField): Price of the booking.
    - payment_status (CharField): Payment status of the booking.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True)


    def clean(self):
        """
        Custom validation method to ensure the start time is before the end time.
        """
        if self.start_time >= self.end_time:
            raise ValidationError("The start time must be before the end time.")

    def __str__(self):
        """
        String representation of the booking.
        """
        return f"Booking for {self.user.username} on {self.date} from {self.start_time} to {self.end_time}"

class Appointment(models.Model):
    """
    Model representing an appointment.
    """
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        """
        String representation of the appointment.
        """
        return self.title

class SpecialEvent(models.Model):
    """
    Model representing a special event.
    """
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()

class TradingHours(models.Model):
    """
    Model representing trading hours for a particular day of the week.
    """
    day_of_week = models.IntegerField(choices=[(i, i) for i in range(7)], unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
