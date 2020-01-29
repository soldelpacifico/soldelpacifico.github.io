from sol.models import Aviso, Noticia, Tarifa, Inicio
from rest_framework import serializers

class AvisoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aviso
        fields = ('dia', 'titulo', 'mensaje')

class NoticiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noticia
        fields = ('fecha_Publicacion', 'titulo', 'texto', 'imagen')

class InicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inicio
        fields = ('lugar',)

class TarifaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarifa
        fields = ('inicio', 'destino', 'valor', 'estudiante')

        