from rest_framework import serializers
from .models import Order  # Assurez-vous d'importer le modèle Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # ou une liste de champs spécifiques
