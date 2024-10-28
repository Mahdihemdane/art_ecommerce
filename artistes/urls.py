from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtisteViewSet

router = DefaultRouter()
router.register(r'artistes', ArtisteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
