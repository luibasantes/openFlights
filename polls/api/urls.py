from django.conf.urls import url
from .views import *

urlpatterns = [
    # Leer aerolineas individuales y Actualizar
    url(r'^aerolinea/(?P<pk>\d+)/$', AerolineaView.as_view(), name='aerolinea'),

    # Lista todas las aerolineas
    url(r'^aerolinea/$', AerolineaListView.as_view(), name='aerolineas'),

    # Crear aerolinea
    url(r'^crear_aerolinea/$', AerolineaCreate.as_view(), name='aerolineas-create'),

    # Leer aeropuertos individuales y Actualizar
    url(r'^aeropuerto/(?P<pk>\d+)/$', AeropuertoView.as_view(), name='aeropuerto'),

    # Lista todas las aeropuertos
    url(r'^aeropuerto/$', AeropuertoListView.as_view(), name='aeropuertos'),

    # Crear aeropuerto
    url(r'^crear_aeropuerto/$', AeropuertoCreate.as_view(), name='aeropuertos-create'),

    # Leer ruta individuales y Actualizar
    url(r'^ruta/(?P<pk>\d+)/$', RutaView.as_view(), name='ruta'),

    # Lista todas las rutas
    url(r'^rutas/$', RutaListView.as_view(), name='rutas'),

    # Crear rutas
    url(r'^crear_ruta/$', RutaCreate.as_view(), name='rutas-create'),
	

	#eliminar deseo
	url(r'^borrar_usuario/(?P<pk>[a-zA-Z]+)$',UsuarioDestroyView.as_view(), name='usuario-delete'),

	# leer lista deseos
    url(r'^lista_deseos/$', UsuarioListView.as_view(), name='UsuarioListView'),

    # Crear deseo
    url(r'crear_deseo/$', CrearDeseoView.as_view(), name='CrearDeseoView')


]