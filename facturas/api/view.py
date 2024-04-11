from facturas.models import Factura
from .serializer import FacturaSerializer
from rest_framework import viewsets


class FacturaView(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer