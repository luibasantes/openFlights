# Generated by Django 2.0 on 2017-12-20 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20171219_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='Destination_airport_ID',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='Source_airport_ID',
            field=models.CharField(max_length=250),
        ),
    ]
