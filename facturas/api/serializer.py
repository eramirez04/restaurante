from rest_framework.serializers import ModelSerializer
from facturas.models import Factura
from productos.api.serializer import ProductoSerializer
from pedidos.api.serializer import PedidosSerializer

from productos.models import Productos


class FacturaSerializer(ModelSerializer):
    productos = ProductoSerializer()
    pedidos = PedidosSerializer()

    class Meta:
        model = Factura
        fields = ['productos', 'pedidos', 'observaciones']
