from sol.models import Aviso, Noticia
from rest_framework import serializers

class AvisoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aviso
        fields = ('dia', 'titulo', 'mensaje')

class NoticiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noticia
        fields = ('fecha_Publicacion', 'titulo', 'texto', 'imagen')