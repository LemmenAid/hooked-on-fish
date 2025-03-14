from django import forms
from .widgets import CustomClearableFileInput
from .models import Product


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating Product instances.

    Includes custom styling for form fields and a custom widget
    for the image field.
    """

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-5'
