import csv,sys,os 
project_dir = "C:/Users/Luigi/Music/openFlights/website"


sys.path.append(project_dir)


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


import django


django.setup()

from polls.models import Ruta,Aeropuerto,Aerolinea



data1 = csv.reader(open("C:/Users/Luigi/Music/openFlights/rutas.csv",encoding="utf-8"),delimiter=',')

for row in data1:
	ruta = Ruta()
	ruta.Airline_ID = row[1]
	print(row[3])
	print(row[5])
	print("----")
	if(row[3]=="\\N"):
		ruta.Source_airport_ID = Aeropuerto.objects.get(Airport_ID = "0")
	else:
		ruta.Source_airport_ID = Aeropuerto.objects.get(Airport_ID = row[3])
	if(row[5]=="\\N"):
		ruta.Destination_airport_ID = Aeropuerto.objects.get(Airport_ID = "0")
	else:
		ruta.Destination_airport_ID = Aeropuerto.objects.get(Airport_ID = row[5])
	
	ruta.Stops = row[7]
	ruta.save()