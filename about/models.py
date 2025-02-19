from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    This model stores details that will be displayed on
    the About page of the website.
    It includes fields for the title, image,
    content, and an updated timestamp.
    The profile image is stored using Cloudinary for media management.
    """
    title = models.CharField(max_length=200)
    about_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    

class Grounds(models.Model):
    """
    This model stores details that will be displayed on
    the Our Fishing Grounds page of the website.
    It includes fields for the title, image,
    content, and an updated timestamp.
    The profile image is stored using Cloudinary for media management.
    """
    title = models.CharField(max_length=200)
    grounds_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title