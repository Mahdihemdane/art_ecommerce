# payment/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='payment_index'),  # Exemple d'une route
]
