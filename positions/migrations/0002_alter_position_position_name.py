# Generated by Django 5.1.2 on 2024-10-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='position_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название должности'),
        ),
    ]
