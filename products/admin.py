from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Product model.

    Defines the fields displayed in the admin panel and sets
    the default ordering by product name.
    """
    list_display = (
        'name',
        'sku',
        'price',
        'image',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
