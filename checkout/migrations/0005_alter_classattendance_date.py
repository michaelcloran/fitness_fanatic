# Generated by Django 4.2.15 on 2024-09-21 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_classattendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classattendance',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
