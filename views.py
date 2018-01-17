from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Aeropuerto
from .models import Aerolinea
from .models import Ruta

def index(request):
	origenes= []
	all_aeropuerto = Aeropuerto.objects.all()
	for aero in all_aeropuerto:
		origenes.append(aero.Country)
	origenes = list(set(origenes))
	origenes.sort()
	destino = origenes
	contenido={"paises":origenes,}
	return render (request,"formulario.html",contenido)

#Vista detallada de cada aeropuerto
def detalle_aeropuerto(request,Airport_ID):
	try:
		aeropuerto = Aeropuerto.objects.get(Airport_ID = str(Airport_ID))
		contenido = contenido={"aeropuerto":aeropuerto,}
	except Aeropuerto.DoesNotExist:
		raise Http404("Aeropuerto no existe")

	return render(request,"modelo_aeropuerto.html",contenido)

#Vista General de todos los Aeropuertos
def aeropuertos(request):
	all_aeropuerto = Aeropuerto.objects.all()
	contenido={"aeropuertos":all_aeropuerto,}

	return render (request,"aeropuertos.html",contenido)

#Vista General de todas las Aerolineas
def aerolinea(request):
	all_aerolinea = Aerolinea.objects.all()
	contenido={"aerolineas":all_aerolinea,}

	return render(request,"aerolineas.html",contenido)

#Vista detallada de cada aerolinea
def detalle_aerolinea(request,Airline_ID):
	try:
		aerolinea = Aerolinea.objects.get(Airline_ID = str(Airline_ID))
		contenido = contenido={"aerolinea":aerolinea,}
	except Aerolinea.DoesNotExist:
		raise Http404("Aerolinea no existe")
	return render(request,"modelo_aerolinea.html",contenido)

def search(request):
	origenes= []
	all_aeropuerto = Aeropuerto.objects.all()
	for aero in all_aeropuerto:
		origenes.append(aero.Country)
	origenes = list(set(origenes))
	origenes.sort()
	destino = origenes
	contenido={"paises":origenes}


	try:
		origen= request.POST["origen"]
		destino = request.POST["destino"]
		bandera_con_escala = request.POST["vuelo"]
		contenido["origen"]=origen
		contenido["destino"]=destino
		if (bandera_con_escala == "0"):
			rutas = Ruta.objects.filter(Stops=0,Source_airport_ID__Country=origen,Destination_airport_ID__Country=destino)
			contenido["vuelo"]="Directo"
		else:
			rutas = Ruta.objects.filter(Stops__gt=0,Source_airport_ID__Country=origen,Destination_airport_ID__Country=destino)
			contenido["vuelo"]="Con Escalas"
		respuesta=[]
		for ruta in rutas:
			try:
				aerolinea = Aerolinea.objects.get(Airline_ID = ruta.Airline_ID)
				if(aerolinea.Active == "Y"):
					opcion = []
					opcion.append(aerolinea.Name)
					opcion.append(ruta.Source_airport_ID.Name)
					opcion.append(ruta.Destination_airport_ID.Name)
					opcion.append(ruta.Stops)
					respuesta.append(opcion)
			except:
				print("algo salio mal")
		if (len(respuesta)==0):
			respuesta=[["N/A","N/A","N/A","N/A"]]
		contenido["resultados"]=respuesta
	except:
		raise Http404("Problemas con el FORMULARIO")
	return render (request,"formulario.html",contenido)


def lista_deseos_read(request):
	return render (request,"lista_deseos_read.html")