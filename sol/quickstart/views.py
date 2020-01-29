from sol.models import Aviso, Noticia, Tarifa, Inicio
from rest_framework import viewsets
from sol.quickstart.serializers import AvisoSerializer, NoticiaSerializer, TarifaSerializer,InicioSerializer

class AvisoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer

class NoticiaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class InicioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Inicio.objects.all()
    serializer_class = InicioSerializer

class TarifaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tarifa.objects.all().order_by('inicio')
    serializer_class = TarifaSerializer
