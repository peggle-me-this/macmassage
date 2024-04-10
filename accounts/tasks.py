# '''
# accounts/tasks.py
# from django.template.loader import render_to_string
# from celery import shared_task
# from django.core.mail import send_mail
# from django.contrib.auth.models import User
# from django.conf import settings

# @shared_task
# def send_registration_confirmation_email(user_id):
#     # Retrieve user details
#     user = User.objects.get(pk=user_id)
    
#     # Render email template
#     subject = 'Registration Confirmation'
#     context = {'user': user}  # Context to pass to the template
#     message = render_to_string('accounts/registration_email.html', context)
    
#     # Compose other email parameters
#     from_email = settings.EMAIL_HOST_USER  # Use your configured email host user
#     to_email = user.email
    
#     # Send email
#     send_mail(subject, message, from_email, [to_email])
# '''