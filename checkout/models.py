import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    Represents an order placed by a customer.

    This model stores all necessary information about the order, including
    customer details, order totals, and shipping information. It also includes
    methods to handle order number generation, total price calculations, and
    custom save behavior.

    Attributes:
        order_number (str): Unique identifier for the order.
        user_profile (ForeignKey): The associated user profile of the customer.
        full_name (str): Full name of the customer.
        email (str): Email address of the customer.
        phone_number (str): Customer's phone number.
        country (CountryField): The country in which the order is placed.
        postcode (str): Postcode for the customer's shipping address.
        town_or_city (str): Town or city for the shipping address.
        street_address1 (str): Primary street address for the shipping.
        street_address2 (str): Secondary street address for shipping.
        county (str): County for the shipping address (optional).
        date (datetime): Date and time the order was placed.
        delivery_cost (Decimal): Cost of delivery for the order.
        order_total (Decimal): Total cost of the items in the order.
        grand_total (Decimal): Total cost of the order, including delivery.
        original_bag (str): Information about the original shopping bag.
        stripe_pid (str): Stripe payment ID used for processing the payment.

    Methods:
        _generate_order_number: Generates a unique order number using UUID.
        update_total: Updates the order total and grand total.
        save: Overridden save method to automatically generate order number.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(
        max_length=40, null=False, blank=False
    )
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Represents an individual line item in an order, which includes
    information about the ordered product, its quantity, and total cost.

    This model serves as a bridge between the `Order` and `Product` models,
    linking a product to a specific order and tracking the quantity ordered
    and the total cost for that product in the order.

    Attributes:
        order (ForeignKey): The order to which this line item belongs.
        product (ForeignKey): The product associated with this line item.
        quantity (int): The number of units of the product ordered.
        lineitem_total (Decimal): The total cost of the line item.

    Methods:
        save: Overrides the default save method to calculate the total cost for
              the line item based on product price and quantity before saving.
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
        )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
