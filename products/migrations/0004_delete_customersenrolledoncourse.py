# Generated by Django 4.2.15 on 2024-09-18 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_customersenrolledoncourse'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomersEnrolledOnCourse',
        ),
    ]
