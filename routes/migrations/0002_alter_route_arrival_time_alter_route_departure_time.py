# Generated by Django 5.1.2 on 2024-10-17 07:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='arrival_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='route',
            name='departure_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]