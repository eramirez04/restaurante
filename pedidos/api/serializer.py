from rest_framework.serializers import ModelSerializer
from productos.api.serializer import ProductosSerializer
from pedidos.models import Pedidos


class PedidosSerializer(ModelSerializer):

    #producto = ProductosSerializer()

    class Meta:
        model = Pedidos
        fields = [
            'id',
            'nombre_comensal',
            'cantidad',
            'producto',
            'estado',
            'preparacion'
        ]

class PedidoSer(ModelSerializer):
    class Meta:
        model = Pedidos