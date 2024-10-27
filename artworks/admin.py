from django.contrib import admin
from .models import Artist, Artwork

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography', 'profile_picture')  # Supprimez 'website' si ce champ n'existe pas
    search_fields = ('name',)

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'price', 'created_at')
    search_fields = ('title',)

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork, ArtworkAdmin)
