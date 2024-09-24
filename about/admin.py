from django.contrib import admin
from .models import About, ContactFormRequest
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    allows editing of the about user
    """
    summernote_fields = ('content',)


@admin.register(ContactFormRequest)
class ContactFormRequestAdmin(admin.ModelAdmin):
    """
    Allows the contact form in admin to be displayed
    with message and a read tick
    """

    list_display = ('message', 'read',)
