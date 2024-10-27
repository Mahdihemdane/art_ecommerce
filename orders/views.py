from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order  # Assurez-vous que vous avez un modèle Order
from .serializers import OrderSerializer  # Assurez-vous que vous avez un serializer
from reportlab.pdfgen import canvas
from django.http import FileResponse
from io import BytesIO
from .models import Order

class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

def generate_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, f"Facture pour la commande {order.id}")
    # Autres informations sur la facture
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'facture_{order.id}.pdf')