from django.db import models
from django.contrib.auth.models import User

from trainers.models import TrainerProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class WorkoutProgram(models.Model):
    trainer = models.ForeignKey(TrainerProfile, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    class_size = models.IntegerField(null=False, blank=False, default=15)
    start_date = models.DateField(null=False, blank=False)
    number_weeks = models.IntegerField(null=False, blank=False, default=12)
    end_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"{self.trainer.user.first_name} {self.trainer.user.last_name}"
