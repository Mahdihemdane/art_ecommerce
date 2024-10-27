from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Vous pouvez ajouter des champs supplémentaires si nécessaire
    is_artist = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_visitor = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username
