# newsletter/tasks.py
'''
from celery import shared_task
from django.core.mail import send_mail
from .models import NewsletterSubscriber, Newsletter

@shared_task
def send_newsletter(newsletter_id):
    """
    Task to send a newsletter to all subscribers.
    """
    newsletter = Newsletter.objects.get(pk=newsletter_id)
    subscribers = NewsletterSubscriber.objects.all()

    subject = newsletter.subject
    message = newsletter.message
    from_email = 'macmassage.za@email.com'  # Update with your email
    recipient_list = [subscriber.email for subscriber in subscribers]

    send_mail(subject, message, from_email, recipient_list)
    '''
