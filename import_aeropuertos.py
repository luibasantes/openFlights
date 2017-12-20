import csv,sys,os 
project_dir = "C:/Users/Luigi/Music/openFlights/website"


sys.path.append(project_dir)


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


import django


django.setup()

from polls.models import Aeropuerto



data1 = csv.reader(open("C:/Users/Luigi/Music/openFlights/aeropuerto.csv",encoding="utf-8"),delimiter=',')

for row in data1:
	aero = Aeropuerto()
	aero.Airport_ID = row[0]
	aero.Name = row[1]
	aero.Country = row[3]
	aero.IATA = row[4]
	aero.ICAO = row[5]
	aero.save()