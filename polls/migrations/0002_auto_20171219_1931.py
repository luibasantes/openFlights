# Generated by Django 2.0 on 2017-12-20 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='Destination_airport_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ARRIVAL', to='polls.Aeropuerto'),
        ),
        migrations.AlterField(
            model_name='route',
            name='Source_airport_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SOURCE', to='polls.Aeropuerto'),
        ),
    ]
