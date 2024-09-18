from django.contrib import admin
from .models import Product, Category, WorkoutProgram

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class WorkoutProgramAdmin(admin.ModelAdmin):
    list_display = (
        'trainer',
        'product',
        'class_size',
        'start_date',
        'number_weeks',
        'end_date',
    )



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkoutProgram, WorkoutProgramAdmin)

