# Generated by Django 2.0 on 2017-12-18 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aerolinea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Airline_ID', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=250)),
                ('Active', models.CharField(max_length=250)),
                ('IATA', models.CharField(max_length=25)),
                ('ICAO', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Airport_ID', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=250)),
                ('Country', models.CharField(max_length=250)),
                ('IATA', models.CharField(max_length=25)),
                ('ICAO', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination_airport_ID', models.CharField(max_length=250)),
                ('Stops', models.CharField(max_length=250)),
                ('Airline_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Aerolinea')),
                ('Source_airport_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Aeropuerto')),
            ],
        ),
    ]