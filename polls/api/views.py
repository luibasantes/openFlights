from rest_framework import generics
from ..models import Aeropuerto, Aerolinea, Ruta
from .serializers import AerolineaSerializer, AeropuertoSerializer, RutaSerializer

#Views para Aerolienas
class AerolineaView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = AerolineaSerializer

    def get_queryset(self):
        return Aerolinea.objects.all()

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


class RutaListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = RutaSerializer

    def get_queryset(self):
        return Ruta.objects.all()


class RutaCreate(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = RutaSerializer

    def get_queryset(self):
        return Ruta.objects.all()

