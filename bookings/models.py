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
'''
from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django_redis import get_redis_connection
from django.conf import settings
from datetime import datetime
from django.core.exceptions import ValidationError


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bookings')  
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True)

    def clean(self):
        # Validate that the start_time is before the end_time
        if self.start_time >= self.end_time:
            raise ValidationError("The start time must be before the end time.")

    def save(self, *args, **kwargs):
        # Perform any custom logic before saving
        # For example, calculate the duration of the booking
        duration = (datetime.combine(datetime.today(), self.end_time) - datetime.combine(datetime.today(), self.start_time)).total_seconds() / 3600
        self.duration_hours = duration
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_profile}'s Booking on {self.date} from {self.start_time} to {self.end_time}"


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AppointmentRescheduleHistory(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='reschedule_history')
    rescheduled_date = models.DateTimeField()
    rescheduled_by = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.appointment} - Rescheduled to {self.rescheduled_date} by {self.rescheduled_by}"
    
class AppointmentRequest(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    requested_date = models.DateField()
    requested_time = models.TimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment request by {self.user_profile.user.email} on {self.requested_date}"

class Config(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.key

class DayOff(models.Model):
    date = models.DateField(unique=True)
    reason = models.TextField()

    def __str__(self):
        return f"Day off on {self.date}"

class EmailVerificationCode(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Verification code {self.code} for {self.user_profile.user.email}"

class PasswordResetToken(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reset token {self.token} for {self.user_profile.user.email}"
'''