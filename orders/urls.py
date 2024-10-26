from django.urls import path
from .views import OrderList  # Importez la classe correctement

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),  # Utilisez .as_view() pour les vues basées sur les classes
]
