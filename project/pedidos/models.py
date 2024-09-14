from django.db import models
from clientes.models import Cliente
from productos.models import ProductoCategoria

class Pedido(models.Model):
    ESTADO = (
        ("PENDIENTE", "Estado que significa que el pedido aún no ha sido revisado"),
        ("EN_PROCESO", "Estado que significa que el pedido está en proceso de revisión"),
        ("COMPLETADO", "Estado que significa que el pedido ha sido completado"),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(ProductoCategoria, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO, default="PENDIENTE")

    def __str__(self) -> str:
        return f"Pedido de {self.producto.nombre} para {self.cliente.nombre}"