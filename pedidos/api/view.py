from rest_framework import viewsets
from rest_framework.views import APIView


from pedidos.models import Pedidos
from .serializer import PedidosSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer



