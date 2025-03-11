from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    """Tests for the home app views."""

    def test_home_page_loads_successfully(self):
        """Home page should load with a 200 status code."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_uses_correct_template(self):
        """Home page should use index.html template."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/index.html')

    def test_home_page_contains_expected_content(self):
        """Check if the home page contains a specific text."""
        response = self.client.get(reverse('home'))
        self.assertContains(response, "We are Hooked on Fish")
