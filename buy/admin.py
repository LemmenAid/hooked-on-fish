from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BuyOnline, BuyInPerson, PartnerShop

admin.site.register(PartnerShop)


@admin.register(BuyOnline)
class BuyOnlineAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model.

    This class customizes the admin interface for the About model by using
    the Summernote editor for the 'content' field.

    Attributes:
    summernote_fields (tuple): Fields that should use the Summernote rich
    text editor. In this case, it's the 'content' field.
    """
    summernote_fields = ('content',)


@admin.register(BuyInPerson)
class BuyInPersonAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model.

    This class customizes the admin interface for the About model by using
    the Summernote editor for the 'content' field.

    Attributes:
    summernote_fields (tuple): Fields that should use the Summernote rich
    text editor. In this case, it's the 'content' field.
    """
    summernote_fields = ('content',)
