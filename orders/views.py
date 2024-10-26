from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order  # Assurez-vous que vous avez un modèle Order
from .serializers import OrderSerializer  # Assurez-vous que vous avez un serializer


class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
