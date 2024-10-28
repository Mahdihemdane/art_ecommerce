from django.db import models

class Artiste(models.Model):
    nom = models.CharField(max_length=100)
    biographie = models.TextField(blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    nationalite = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom
