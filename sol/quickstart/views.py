from sol.models import Aviso, Noticia
from rest_framework import viewsets
from sol.quickstart.serializers import AvisoSerializer, NoticiaSerializer

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
