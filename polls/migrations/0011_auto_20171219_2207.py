# Generated by Django 2.0 on 2017-12-20 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20171219_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='Airline_ID',
            field=models.CharField(max_length=250),
        ),
    ]
