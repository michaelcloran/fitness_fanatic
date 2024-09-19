from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_trainer, name='add_trainer'),
    path('alltrainers/', views.view_trainers, name='view_trainers'),
    path('trainerdetails/<int:trainer_id>', views.trainer_detail, name='trainer_detail'),
    path('edittrainer/<int:trainer_id>', views.edit_trainer, name='edit_trainer'),
    path('delete/<int:trainer_id>/', views.delete_trainer, name='delete_trainer'),
    path('contacttrainer/<int:trainer_id>/', views.contact_trainer, name='contact_trainer'),
]