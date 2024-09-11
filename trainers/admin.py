from django.contrib import admin
from .models import TrainerProfile
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(TrainerProfile)
class TrainerAdmin(SummernoteModelAdmin):
    """
    allows editing of the about user
    """
    summernote_fields = ('content',)

