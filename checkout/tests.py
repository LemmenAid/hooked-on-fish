from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.conf import settings
from unittest.mock import patch

import json

from checkout.models import Order
from products.models import Product


# ------------ VIEWS TESTING ------------
class CheckoutViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.order_url = reverse('checkout')
        self.success_url = reverse('checkout_success', args=['12345'])
        self.cache_url = reverse('cache_checkout_data')

        self.session = self.client.session
        self.session['bag'] = {str(self.product.id): 1}
        self.session.save()

    @patch('stripe.PaymentIntent.create')
    def test_checkout_get(self, mock_stripe_intent):
        mock_stripe_intent.return_value.client_secret = 'test_secret'
        response = self.client.get(self.order_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertIn('order_form', response.context)

    @patch('stripe.PaymentIntent.create')
    def test_checkout_post_valid_order(self, mock_stripe_intent):
        mock_stripe_intent.return_value.client_secret = 'test_secret'
        self.client.login(username='testuser', password='testpass')
        form_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'country': 'IE',
            'postcode': '00000',
            'town_or_city': 'Test Town',
            'street_address1': '123 Test St',
            'street_address2': '',
            'county': 'Test County',
            'client_secret': 'pi_12345_secret_test'
        }
        response = self.client.post(self.order_url, form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Order.objects.exists())

    @patch('stripe.PaymentIntent.modify')
    def test_cache_checkout_data(self, mock_stripe_modify):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.cache_url, {
            'client_secret': 'pi_12345_secret_test',
            'save_info': 'on'
        })
        self.assertEqual(response.status_code, 200)
        mock_stripe_modify.assert_called_once()

    def test_checkout_success(self):
        order = Order.objects.create(
            order_number='12345',
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            country='IE',
            town_or_city='Test Town',
            street_address1='123 Test St'
        )
        response = self.client.get(reverse(
            'checkout_success', args=[order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Order successfully processed!' in str(m) for m in messages))
