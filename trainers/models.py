from django.contrib.auth.models import User
from django.db import models


class TrainerProfile(models.Model):
    """ A trainer profile for managing trainers """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=False, blank=False)
    bio = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class ContactTrainerRequest(models.Model):
    """ This will allow an avenue to contact a particular trainer
    with a request in relation to a workout program
    """
    trainer = models.ForeignKey(TrainerProfile, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date_time = models.DateTimeField(auto_now=True)
    message = models.TextField(null=False, blank=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact Trainer request from {self.name}"
