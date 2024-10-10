# Generated by Django 5.1.2 on 2024-10-10 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crew_directory', '0001_initial'),
        ('stations', '0001_initial'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('arrival_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arrival_station', to='stations.station')),
                ('crew', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crew_directory.crewdirectory')),
                ('departure_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departure_station', to='stations.station')),
                ('owner_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner_station', to='stations.station')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trains.train')),
            ],
        ),
    ]
