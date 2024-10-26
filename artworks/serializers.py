from rest_framework import serializers
from .models import Artwork  # Assurez-vous que ce modèle est défini dans models.py

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = '__all__'  # Ou une liste de champs spécifiques
