from rest_framework import serializers
from ..models import Aerolinea, Aeropuerto, Ruta, Usuario

class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aerolinea
        fields = '__all__'


class AeropuertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeropuerto
        fields = '__all__'


class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'
	
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Usuario
		fields=('nombres','celular','f_partida','f_retorno','ciudad_partida','ciudad_llegada','escala')
	