from django.urls import path
from django.conf.urls import url
from . import views	

app_name = "polls"

urlpatterns = [
	#Busqueda 127.0.0.1:8000/vuelos
    url(r'^$', views.index, name='index'),
	
	#Busqueda 127.0.0.1:8000/vuelos/aeropuertos/
	url(r'^aeropuertos/$', views.aeropuertos, name='Aeropuertos'),
	
	#Busqueda 127.0.0.1:8000/vuelos/aeropuertos/#Airport_ID
	url(r'^aeropuertos/(?P<Airport_ID>[0-9]+)/$', views.detalle_aeropuerto, name='Aeropuerto'),
	
	#Busqueda 127.0.0.1:8000/vuelos/aerolineas/
	url(r'^aerolineas/$', views.aerolinea, name='Aerolineas'),
	
	#Busqueda 127.0.0.1:8000/vuelos/aerolineas/#Airline_ID
	url(r'^aerolineas/(?P<Airline_ID>[-]?[0-9]+)/$', views.detalle_aerolinea, name='Aerolinea'),
	
	#Busqueda 127.0.0.1:8000/vuelos/search/
    url(r'^search/$', views.search, name='search'),
	
	#Busqueda 127.0.0.1:8000/vuelos/search/
    url(r'^lista_deseos/$', views.lista_deseos_read, name='lista_deseos'),

	#Crear deseo 127.0.0.1:8000/crear_deseo
	url(r'^crear_deseo/$', views.crear_deseo, name='crear_deseos'),
]
