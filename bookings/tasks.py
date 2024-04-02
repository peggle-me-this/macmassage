# bookings/tasks.py
'''
will reconnect if email is needed as a feature in the future
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Booking

@shared_task
def send_booking_confirmation_email(booking_id):
    booking = Booking.objects.get(pk=booking_id)
    subject = 'Booking Confirmation'
    message = f'Hi {booking.customer_name},\n\nYour booking for {booking.date_time} has been confirmed.'
    from_email = 'macmassage.za@gmail.com'
    to_email = booking.customer_email
    send_mail(subject, message, from_email, [to_email])

@shared_task
def send_booking_reminder_email(booking_id):
    booking = Booking.objects.get(pk=booking_id)
    reminder_time = booking.date_time - timezone.timedelta(hours=24)
    if timezone.now() >= reminder_time:
        subject = 'Booking Reminder'
        message = f'Hi {booking.customer_name},\n\nThis is a reminder for your booking tomorrow at {booking.date_time}.'
        from_email = 'macmassage.za@gmail.com'
        to_email = booking.customer_email
        send_mail(subject, message, from_email, [to_email])
'''