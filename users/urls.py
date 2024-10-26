from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtworkViewSet, CartViewSet

router = DefaultRouter()
router.register(r'artworks', ArtworkViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
