from rest_framework import viewsets
from .models import Artiste
from .serializers import ArtisteSerializer

class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
