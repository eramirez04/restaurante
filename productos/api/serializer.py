from rest_framework.serializers import ModelSerializer
from productos.models import Productos


class ProductosSerializer(ModelSerializer):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'cantidad', 'precio']


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Productos
        fields = ['nombre','precio']