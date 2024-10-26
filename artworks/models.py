# artworks/models.py

from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/')  # Assurez-vous que MEDIA_URL et MEDIA_ROOT sont configurés

    def __str__(self):
        return self.title
