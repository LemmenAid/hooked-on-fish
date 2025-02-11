from django.db import models


class Contact(models.Model):
    """
    This model stores information about users who reach out, including their
    name, email, gardening experience level, garden zone, message, and whether
    the request has been read.
    """
    TOPIC_CHOICES = [
        ('registration', 'Register / Sign Up'),
        ('order', 'Order Inquiry'),
        ('products', 'About the Products'),
        ('sustainability', 'Sustainability & Sourcing'),
        ('other', 'Other'),
    ]

    REFERRAL_CHOICES = [
        ('social_media', 'Social Media'),
        ('friend_family', 'Friend or Family'),
        ('market', 'Local Market or Shop'),
        ('website', 'Our Website'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    topic_choices = models.CharField(
        max_length=50,
        choices=TOPIC_CHOICES,
        default='other',
        verbose_name="What is your question about?"
    )
    referral_source = models.CharField(
        max_length=50,
        choices=REFERRAL_CHOICES,
        default='other',
        verbose_name="How did you hear about Hooked on Fish?"
    )
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact request from {self.name}"
