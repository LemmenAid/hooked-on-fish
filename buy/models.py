from django.db import models
from cloudinary.models import CloudinaryField


class BuyOnline(models.Model):
    """
    This model stores details that will be displayed on
    the Buy Online page of the website.
    It includes fields for the title, profile image,
    content, and an updated timestamp.
    The about image is stored using Cloudinary for media management.
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class BuyInPerson(models.Model):
    """
    This model stores details that will be displayed on
    the Buy in Person page of the website.
    It includes fields for the title, profile image,
    content, and an updated timestamp.
    The grounds image is stored using Cloudinary for media management.
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class PartnerShop(models.Model):
    """
    This model stores details about partner shops that sell Hooked on Fish products.
    """
    name = models.CharField(max_length=255)
    address = models.TextField()
    website = models.URLField(blank=True, null=True)
    buy_in_person = models.ForeignKey(
        BuyInPerson, on_delete=models.CASCADE, related_name="partner_shops"
    )

    def __str__(self):
        return self.name
