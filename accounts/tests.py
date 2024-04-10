from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import ProfileEditForm
from django.core import mail
from django.core.mail import send_mail

User = get_user_model()

class EmailTestCase(TestCase):
    def test_send_email(self):
        send_mail(
            'Subject here',
            'Here is the message.',
            'macmassage.za@gmail.com',
            ['bronwyn.d.barnes@gmail.com'],
            fail_silently=False,
        )
        # Check that the email was sent
        self.assertEqual(len(mail.outbox), 1)
        # Verify the email contents
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
        self.assertEqual(mail.outbox[0].body, 'Here is the message.')
        self.assertEqual(mail.outbox[0].from_email, 'macmassage.za@gmail.com')
        self.assertEqual(mail.outbox[0].to, ['bronwyn.d.barnes@gmail.com'])


    def test_profile_edit_form_valid(self):
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
        }
        form = ProfileEditForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_edit_form_invalid(self):
        form_data = {
            'first_name': '',
            'last_name': 'User',
        }
        form = ProfileEditForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_profile_edit_view(self):
        response = self.client.post(reverse('accounts:edit_profile'), {
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertEqual(response.status_code, 302)  # Check for successful redirect after profile edit

    # Add more tests as needed


