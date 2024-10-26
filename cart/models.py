from django.db import models
from users.models import User  # Assurez-vous que User est bien défini dans votre modèle Users
from artworks.models import Artwork  # Si Artwork est dans une autre application, importez-le ici

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart of {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)  # Exemple de champ nullable
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.artwork.title}'
