# Generated by Django 5.1.2 on 2024-10-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='stations',
            field=models.ManyToManyField(related_name='trains', to='stations.station'),
        ),
    ]