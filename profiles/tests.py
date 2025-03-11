from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import UserProfile
from checkout.models import Order


class ProfileViewTests(TestCase):
    def setUp(self):
        """Set up a test user and profile."""
        self.user = User.objects.create_user(
            username='testuser', password='password123')
        self.profile = UserProfile.objects.get(user=self.user)
        self.client.login(username='testuser', password='password123')

    def test_profile_page_loads(self):
        """Test that the profile page loads correctly for a logged-in user."""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'My Profile')

    def test_profile_update_success(self):
        """Test that a valid profile update saves successfully."""
        form_data = {
            'default_phone_number': '123456789',
            'default_street_address1': '123 Main St',
            'default_town_or_city': 'Galway',
            'default_postcode': 'H91ABC',
            'default_county': 'Galway County',
            'default_country': 'IE',
        }
        response = self.client.post(
            reverse('profile'), data=form_data, follow=True)
        self.profile.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile updated successfully')
        self.assertEqual(self.profile.default_town_or_city, 'Galway')

    def test_profile_update_invalid(self):
        """Test that an invalid profile update shows an error."""
        form_data = {
            'default_country': '',  # Required field left blank
            'default_street_address1': '123 Main St',
        }
        response = self.client.post(reverse('profile'), data=form_data)
        self.assertEqual(response.status_code, 200)


class OrderHistoryViewTests(TestCase):
    def setUp(self):
        """Set up a test user, profile, and order."""
        self.user = User.objects.create_user(
                username='testuser', password='password123')
        self.profile = UserProfile.objects.get(user=self.user)
        self.order = Order.objects.create(
            user_profile=self.profile, order_number='12345', grand_total=50.00)
        self.client.login(username='testuser', password='password123')

    def test_order_history_access(self):
        """Test that a user can access their past order details."""
        response = self.client.get(reverse('order_history', args=['12345']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(
            response, 'This is a past confirmation for order number 12345')
        self.assertContains(response, '€50.00')
