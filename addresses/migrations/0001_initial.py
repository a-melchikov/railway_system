# Generated by Django 5.1.2 on 2024-10-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='Улица')),
                ('house', models.CharField(blank=True, max_length=10, null=True, verbose_name='Дом')),
                ('apartment', models.CharField(blank=True, max_length=10, null=True, verbose_name='Квартира')),
            ],
        ),
    ]
