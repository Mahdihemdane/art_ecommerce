from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart.views import CartViewSet
from artworks.views import ArtworkViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'artworks', ArtworkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Cela inclut toutes les routes définies dans le router
]
