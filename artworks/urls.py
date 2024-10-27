from django.urls import path
from .views import ArtworkListView, ArtworkDetailView, ArtistListView, ArtistDetailView

urlpatterns = [
    path('artworks/', ArtworkListView.as_view(), name='artwork-list'),
    path('artworks/<int:pk>/', ArtworkDetailView.as_view(), name='artwork-detail'),
    path('artists/', ArtistListView.as_view(), name='artist-list'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
]
