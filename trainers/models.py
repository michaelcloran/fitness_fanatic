from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class TrainerProfile(models.Model):
    """ A trainer profile for managing trainers """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=False, blank=False)
    bio = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"