from rest_framework import viewsets
from productos.models import Productos
from .serializer import ProductosSerializer


class ProductosModelViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
