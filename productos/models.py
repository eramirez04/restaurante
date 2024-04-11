from django.db import models


# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nombre