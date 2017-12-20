import csv,sys,os 
project_dir = "C:/Users/Luigi/Music/openFlights/website"


sys.path.append(project_dir)


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


import django


django.setup()

from polls.models import Aerolinea



data1 = csv.reader(open("C:/Users/Luigi/Music/openFlights/aerolineas.csv",encoding="utf-8"),delimiter=',')

for row in data1:
	aerolinea = Aerolinea()
	aerolinea.Airline_ID = row[0]
	aerolinea.Name = row[1]
	aerolinea.Active = row[7]
	aerolinea.IATA = row[3]
	aerolinea.ICAO = row[4]
	aerolinea.save()