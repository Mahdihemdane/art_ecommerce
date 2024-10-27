from rest_framework import serializers
from .models import Cart  # Assurez-vous que l'importation est correcte
from users.models import Artwork  # Importez Artwork si nécessaire

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
