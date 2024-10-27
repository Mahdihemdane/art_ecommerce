from rest_framework import serializers
from .models import Artwork, Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'user', 'bio', 'website']  # Ajoutez les champs que vous souhaitez exposer

class ArtworkSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Artwork
        fields = ['id', 'title', 'description', 'image', 'price', 'artist', 'created_at', 'updated_at']
