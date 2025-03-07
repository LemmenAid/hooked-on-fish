from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    """
    Represents a product available for purchase.

    **Fields:**
    - `sku`: Optional stock-keeping unit identifier.
    - `name`: Name of the product.
    - `description`: Detailed description of the product.
    - `caught_in_these_waters`: Location where the product was sourced,
       defaults to 'Derryinver Bay'.
    - `price`: Product price as a decimal value.
    - `image_url`: Cloudinary field for storing the product image,
       defaults to a placeholder.
    - `image`: Optional image upload field.

    **Methods:**
    - `__str__()`: Returns the product name as its string representation.
    """
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    caught_in_these_waters = models.CharField(
        max_length=254, default="Derryinver Bay"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = CloudinaryField('image', default='placeholder')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
