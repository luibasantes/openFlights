# Generated by Django 2.0 on 2017-12-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20171219_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='Stops',
            field=models.BigIntegerField(),
        ),
    ]
