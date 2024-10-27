from django.db import models
from django.conf import settings
from cart.models import Cart  # Assurez-vous d'importer le modèle Cart

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')  # Nom unique pour éviter les conflits
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')  # Lien vers le cart
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix total de la commande
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création de la commande
    updated_at = models.DateTimeField(auto_now=True)  # Date de mise à jour de la commande

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
