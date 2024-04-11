from django.db import models
from productos.models import Productos
from pedidos.models import Pedidos


class Factura(models.Model):
    observaciones = models.CharField(max_length=200)
    productos = models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True)
    pedidos = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
