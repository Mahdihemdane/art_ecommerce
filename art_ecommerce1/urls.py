
# art_ecommerce1/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart.views import CartViewSet  # Exemple d'importation

# Créez un routeur
router = DefaultRouter()
router.register(r'cart', CartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Assurez-vous que c'est correct
]
