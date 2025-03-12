from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient
from rest_framework import status
from django.core import mail
from .models import Contact

class ContactAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "number": "9876543210",
            "message": "I need help with my order."
        }
        self.invalid_payload = {
            "name": "",
            "email": "invalidemail",
            "number": "123",
            "message": ""
        }

    def test_contact_form_submission_success(self):
        """Test successful submission of the contact form."""
        response = self.client.post('/api/contact/', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Contact Form Submitted Successfully")

        # Verify the contact is saved in the database
        contact = Contact.objects.get(email=self.valid_payload['email'])
        self.assertEqual(contact.name, self.valid_payload['name'])

        # Verify email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Thank You for Contacting Us")
        self.assertIn("Dear John Doe,", mail.outbox[0].body)

    def test_contact_form_submission_failure(self):
        """Test submission of invalid contact form data."""
        response = self.client.post('/api/contact/', self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertIn('number', response.data)
        self.assertIn('message', response.data)

        # Verify no email was sent
        self.assertEqual(len(mail.outbox), 0)

    def test_missing_required_fields(self):
        """Test missing required fields in the form."""
        incomplete_payload = {
            "name": "John Doe",
            "email": "",
            "number": "",
            "message": ""
        }
        response = self.client.post('/api/contact/', incomplete_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertIn('number', response.data)
        self.assertIn('message', response.data)
