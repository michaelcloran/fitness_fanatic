from django.contrib import admin
from .models import TrainerProfile, ContactTrainerRequest
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(TrainerProfile)
class TrainerAdmin(SummernoteModelAdmin):
    """
    allows editing of the about user
    """
    summernote_fields = ('content',)

@admin.register(ContactTrainerRequest)
class ContactTrainerRequestAdmin(admin.ModelAdmin):
    """
    Allows the trainer contact form in admin to be displayed
    with message and a read tick
    """

    list_display = ('trainer', 'name', 'message', 'date_time', 'read',)