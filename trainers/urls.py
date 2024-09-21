from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_trainer, name='add_trainer'),
    path('alltrainers/', views.view_trainers, name='view_trainers'),
    path('trainerdetails/<int:trainer_id>', views.trainer_detail, name='trainer_detail'),
    path('edittrainer/<int:trainer_id>', views.edit_trainer, name='edit_trainer'),
    path('delete/<int:trainer_id>/', views.delete_trainer, name='delete_trainer'),
    path('contacttrainer/<int:trainer_id>/', views.contact_trainer, name='contact_trainer'),
    path('traineremail/<int:trainer_id>/', views.view_trainer_email, name='view_trainer_email'),
    path('updatetraineremail/<int:email_id>/', views.update_trainer_email, name='update_trainer_email'),
    path('trainercourses/', views.view_trainer_courses, name='view_trainer_courses'),
    path('classAttendance/<int:wo_program_id>/', views.view_class_attendance, name='view_class_attendance'),
]