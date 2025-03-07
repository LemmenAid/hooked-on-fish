from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom file input widget for product images.

    **Features:**
    - Overrides Django’s `ClearableFileInput` to customize labels.
    - Displays a "Remove" checkbox for existing images.
    - Shows "Current Image" next to the existing file.
    - Uses a custom template for rendering.

    **Customization:**
    - `clear_checkbox_label`: Label for the remove checkbox.
    - `initial_text`: Label for the currently uploaded image.
    - `input_text`: No label for the file input field.
    - `template_name`: Path to the custom template for rendering.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/'
        'custom_clearable_file_input.html'
    )
