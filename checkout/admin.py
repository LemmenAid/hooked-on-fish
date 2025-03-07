from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Admin configuration for OrderLineItem.

    This inline admin allows OrderLineItem instances to be displayed
    within the Order admin panel. The `lineitem_total` field is
    set to readonly to prevent manual edits.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Order model.

    This class customizes the Order model's admin interface, including:
    - Displaying OrderLineItem instances inline.
    - Setting readonly fields to prevent modifications of key fields.
    - Defining the order of fields in the detail view.
    - Specifying fields to display in the order list.
    - Ordering orders by most recent date.

    Readonly fields ensure that financial and transactional data
    remain consistent and protected from accidental changes.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
