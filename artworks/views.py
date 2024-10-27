from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Artwork
from .serializers import ArtworkSerializer
from rest_framework.response import Response
from rest_framework import status

class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [IsAuthenticated]  # Assurez-vous que l'utilisateur est authentifié

    def list(self, request):
        artworks = self.get_queryset()
        serializer = self.get_serializer(artworks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        artwork = self.get_object()
        serializer = self.get_serializer(artwork)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(artist=request.user.artist)  # Assurez-vous que l'artiste est défini correctement
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        artwork = self.get_object()
        serializer = self.get_serializer(artwork, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        artwork = self.get_object()
        artwork.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
