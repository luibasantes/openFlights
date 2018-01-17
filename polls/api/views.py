from rest_framework import generics
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

