from django.db import models
from productos.models import Productos


class Pedidos(models.Model):
    class Status(models.TextChoices):
        PENDIENTE = 'preparacion', 'preparacion'
        ENTREGADO = 'entregado', 'entregado'

    class Entrega(models.TextChoices):
        LLEVAR = 'llevar', 'llevar'
        CONSUMIR = 'consumir en restaurante', 'consumir en restaurante'

    nombre_comensal = models.CharField(max_length=100)
    cantidad = models.PositiveBigIntegerField()

    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True)

    estado = models.CharField(max_length=11, choices=Status.choices, default=Status.PENDIENTE)
    preparacion = models.CharField(max_length=23, choices=Entrega.choices, default=Entrega.CONSUMIR)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_pedido']

    def __str__(self):
        return self.cantidad
