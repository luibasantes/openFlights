from rest_framework import generics,status
from rest_framework.response import Response
from ..models import Aeropuerto, Aerolinea, Ruta, Usuario
from .serializers import *

#Views para Aerolienas
class AerolineaView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = AerolineaSerializer

    def get_queryset(self):
        return Aerolinea.objects.all()

    def get_object(self):
        aero_id = self.kwargs.get("pk")
        return Aerolinea.objects.get(Airline_ID=aero_id)

class AerolineaListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AerolineaSerializer

    def get_queryset(self):
        return Aerolinea.objects.all()

class AerolineaCreate(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = AerolineaSerializer

    def get_queryset(self):
        return Aerolinea.objects.all()


#Views para Aeropuerto
class AeropuertoView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = AeropuertoSerializer

    def get_queryset(self):
        return Aeropuerto.objects.all()

    def get_object(self):
        aerop_id = self.kwargs.get("pk")
        return Aerolinea.objects.get(Airport_ID=aerop_id)


class AeropuertoListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AeropuertoSerializer

    def get_queryset(self):
        return Aeropuerto.objects.all()


class AeropuertoCreate(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = AeropuertoSerializer

    def get_queryset(self):
        return Aeropuerto.objects.all()


#Views para Rutas
class RutaView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = RutaSerializer

    def get_queryset(self):
        return Ruta.objects.all()

    def get_object(self):
        aerop_id = self.kwargs.get("pk")
        return Aerolinea.objects.get(Airport_ID=aerop_id)


class RutaListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = RutaSerializer

    def get_queryset(self):
        return Ruta.objects.all()

class UsuarioListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return Usuario.objects.all()

class RutaCreate(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = RutaSerializer

    def get_queryset(self):
        return Ruta.objects.all()

#Views para Deseo

class UsuarioDestroyView(generics.DestroyAPIView):
	lookup_field='pk'
	serializer_class= UsuarioSerializer
	
	def get_queryset(self):
		return Usuario.objects.all()
		
	def get_object(self):
		nombre = self.kwargs.get("pk")
		print("nombre:",nombre)
		return Usuario.objects.get(nombres=nombre)
	
	def delete(self,request,*args,**kwargs):
		return self.destroy(request, *args, **kwargs)
	
	def destroy(self,request,*args,**kwargs):
		instance = self.get_object()
		print("this instance:",instance)
		self.perform_destroy(instance)
		return Response(status=status.HTTP_204_NO_CONTENT)


class CrearDeseoView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return Usuario.objects.all()
		
class ModificarDeseoView(generics.UpdateAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer
	lookup_field = 'pk'
	
	def get_object(self):
		nombre = self.kwargs.get("pk")
		print("nombre:",nombre)
		return Usuario.objects.get(nombres=nombre)
	
	def put(self, request, pk, format=None):
		user = self.get_object()
		serializer= UsuarioSerializer(user, data=request.data)
		print(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
