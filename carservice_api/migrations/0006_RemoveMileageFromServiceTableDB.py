# Generated by Django 4.1.7 on 2024-01-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carservice_api', '0005_MakeDescriptionAndMileagNullableServiceTableDB'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='mileage',
        ),
        migrations.AddField(
            model_name='maintenance',
            name='mileage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
