# orders/models.py

from django.conf import settings
from django.db import models

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Référence à l'utilisateur
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création de la commande
    updated_at = models.DateTimeField(auto_now=True)  # Date de mise à jour de la commande
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix total de la commande
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')  # Statut de la commande

    def __str__(self):
        return f"Order {self.id} by {self.user.username} - Status: {self.status}"

# orders/models.py

from django.db import models
from django.conf import settings

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    Artwork = models.ForeignKey('artworks.artwork', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Ajout d'une valeur par défaut


    def __str__(self):
        return f"Item {self.artwork.title} (x{self.quantity}) in Order {self.order.id}"
