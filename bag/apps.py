from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    Configuration for the Bag app.

    This app handles shopping bag functionality, including adding, updating,
    and removing items from the user's cart.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
