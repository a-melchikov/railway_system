# Generated by Django 5.1.2 on 2024-10-10 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('train_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('train_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='train_types.traintype')),
            ],
        ),
    ]