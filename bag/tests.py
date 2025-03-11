from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from products.models import Product


class BagViewsTests(TestCase):
    """Tests for the shopping bag views"""

    def setUp(self):
        """Create a test product and a client"""
        self.client = Client()
        self.product = Product.objects.create(
            name="Test Fish",
            description="Fresh and tasty fish",
            price=10.00
        )

    def test_view_bag(self):
        """Test if the bag page loads correctly"""
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        """Test adding an item to the bag"""
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {'quantity': 1, 'redirect_url': reverse('view_bag')}
        )
        self.assertRedirects(response, reverse('view_bag'))
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 1)

    def test_add_to_bag_max_quantity(self):
        """Test adding an item exceeding max quantity (20)"""
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {'quantity': 25, 'redirect_url': reverse('view_bag')}
        )
        self.assertRedirects(response, reverse('view_bag'))
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 20)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(
            messages[0]), f"Maximum quantity for {self.product.name} =20."
                           "Quantity set to 20.")

    def test_add_to_bag_invalid_quantity(self):
        """Test adding a non-integer quantity"""
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {'quantity': 'invalid', 'redirect_url': reverse('view_bag')}
        )
        self.assertRedirects(response, reverse('view_bag'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Invalid quantity entered.")

    def test_adjust_bag(self):
        """Test adjusting an item's quantity in the bag"""
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        response = self.client.post(
            reverse('adjust_bag', args=[self.product.id]),
            {'quantity': 3}
        )
        self.assertRedirects(response, reverse('view_bag'))
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 3)

    def test_adjust_bag_remove_item(self):
        """Test removing an item by setting its quantity to 0"""
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        response = self.client.post(
            reverse('adjust_bag', args=[self.product.id]),
            {'quantity': 0}
        )
        self.assertRedirects(response, reverse('view_bag'))
        self.assertNotIn(str(self.product.id), self.client.session['bag'])

    def test_remove_from_bag(self):
        """Test removing an item from the bag"""
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        response = self.client.post(
            reverse('remove_from_bag', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(str(self.product.id), self.client.session['bag'])

    def test_remove_from_bag_invalid_product(self):
        """Test removing a non-existent item"""
        response = self.client.post(
            reverse('remove_from_bag', args=[9999]))  # ID that doesn't exist
        self.assertEqual(response.status_code, 500)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn("Error removing item", str(messages[0]))
