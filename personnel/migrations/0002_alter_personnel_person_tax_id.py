# Generated by Django 5.1.2 on 2024-10-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='person_tax_id',
            field=models.CharField(db_index=True, max_length=12, primary_key=True, serialize=False),
        ),
    ]