# Generated by Django 2.0 on 2017-12-20 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20171219_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='Destination_airport_ID',
        ),
    ]
