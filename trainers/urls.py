from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_trainer, name='add_trainer'),
]