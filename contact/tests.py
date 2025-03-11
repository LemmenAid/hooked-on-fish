from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Contact
from .forms import ContactForm


class ContactModelTests(TestCase):
    """Test the Contact model."""

    def test_create_contact(self):
        """Ensure a Contact instance can be created successfully."""
        contact = Contact.objects.create(
            name="Thomas Coyle",
            email="t.coyle@example.com",
            topic_choices="order",
            referral_source="website",
            message="I have a question about my order."
        )
        self.assertEqual(contact.name, "Thomas Coyle")
        self.assertEqual(contact.email, "t.coyle@example.com")
        self.assertEqual(contact.topic_choices, "order")
        self.assertEqual(contact.referral_source, "website")
        self.assertEqual(contact.message, "I have a question about my order.")
        self.assertFalse(contact.read)


class ContactFormTests(TestCase):
    """Test the Contact form."""

    def test_valid_form(self):
        """Form should be valid when all required fields are provided."""
        form_data = {
            "name": "Jane Coyle",
            "email": "jane@example.com",
            "topic_choices": "sustainability",
            "referral_source": "social_media",
            "message": "Tell me more about sustainability efforts."
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        """Form should be invalid if required fields are missing."""
        form_data = {
            "name": "",  # Missing name
            "email": "invalid-email",  # Invalid email format
            "topic_choices": "order",
            "referral_source": "website",
            "message": "Inquiry about my order."
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("email", form.errors)


class ContactViewTests(TestCase):
    """Test the Contact Us view."""

    def test_contact_page_loads(self):
        """Ensure the contact page loads with the form."""
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertIsInstance(response.context["contact_form"], ContactForm)

    def test_valid_contact_submission(self):
        """
        Submitting a valid form should save contact request
        and show a success message.
        """
        form_data = {
            "name": "Alice Smith",
            "email": "alice@example.com",
            "topic_choices": "products",
            "referral_source": "market",
            "message": "What are your best products?"
        }
        response = self.client.post(reverse(
            "contact"), data=form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, "Alice Smith")

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "Contact request received!"
                              " We endeavour to respond within 2 days.")

    def test_invalid_contact_submission(self):
        """Invalid form submission should not save and should return errors."""
        form_data = {
            "name": "",  # Missing required field
            "email": "wrongemail",  # Invalid email format
            "topic_choices": "order",
            "referral_source": "website",
            "message": "Missing name and invalid email."
        }
        response = self.client.post(reverse("contact"), data=form_data)

        # Page should reload with a 200 status (not redirect)
        self.assertEqual(response.status_code, 200)

        # Database should not save invalid submissions
        self.assertEqual(Contact.objects.count(), 0)

        # Check if error messages are displayed
        self.assertContains(response, "This field is required.")
        self.assertContains(response, "Enter a valid email address.")

        # Check if form is still populated
        self.assertContains(response, "Missing name and invalid email.")
