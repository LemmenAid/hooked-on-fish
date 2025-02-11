from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for capturing contact information and gardening-related inquiries.

    This form is used to collect a user's name, email, gardening experience,
    garden zone, and a message. The garden zone field is presented as a custom
    choice field with a link to a zone map.

    Attributes:
        garden_zone (GardenZoneField): Custom field for selecting
        the gardening zone.
    """
    class Meta:
        model = Contact
        fields = ('name', 'email', 'topic_choices',
                  'referral_source', 'message')
