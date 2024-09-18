# Generated by Django 4.2.15 on 2024-09-18 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_customersenrolledoncourse'),
        ('checkout', '0002_order_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomersEnrolledOnCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('order_line_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.orderlineitem')),
                ('wo_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.workoutprogram')),
            ],
        ),
    ]
