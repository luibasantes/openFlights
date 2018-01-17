from django.db import models

# Create your models here.
class Aeropuerto(models.Model):
	
	Airport_ID = models.CharField(max_length=250)
	Name = models.CharField(max_length=250)
	#City = models.CharField(max_lenght=250)
	Country = models.CharField(max_length=250)
	IATA = models.CharField(max_length=25)
	ICAO = models.CharField(max_length=25)
	#Latitude = models.CharField(max_lenght=250)
	#Longitude = models.CharField(max_lenght=250)
	#Altitude = models.CharField(max_lenght=250)
	#Timezone = models.CharField(max_lenght=250)
	#DST = models.CharField(max_lenght=250)
	#Tz = models.CharField(max_lenght=250)
	#Type = models.CharField(max_lenght=250)
	#Source = models.CharField(max_lenght=250)
	
	def __str__(self):
		return self.Name +" -- " + self.Country
	
	
class Aerolinea(models.Model):
	
	Airline_ID = models.CharField(max_length=250)
	Name = models.CharField(max_length=250)
	#City = models.CharField(max_lenght=250)
	Active = models.CharField(max_length=250)
	IATA = models.CharField(max_length=25)
	ICAO = models.CharField(max_length=25)
	
	def __str__(self):
		return self.Name +" -- " + self.Active
	
		

class Ruta(models.Model):
	Airline_ID = models.CharField(max_length=250)
	Source_airport_ID = models.ForeignKey(Aeropuerto,related_name='SRC',on_delete=models.CASCADE,)
	Destination_airport_ID = models.ForeignKey(Aeropuerto,on_delete=models.CASCADE,)
	Stops = models.BigIntegerField()


class Usuario(models.Model):
	nombres = models.CharField(max_length=250)
	celular = models.IntegerField(default=0)
	f_partida = models.DateTimeField()
	f_retorno = models.DateTimeField()
	ciudad_partida = models.CharField(max_length=100)
	ciudad_llegada = models.CharField(max_length=100)
	escala = models.BooleanField(default=True)

