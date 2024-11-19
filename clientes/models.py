from django.db import models
from django.urls import reverse


# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


# Modelo Cliente
class Cliente(models.Model):
    TIPOS_CLIENTE = [
        ('consignacion', 'Consignación'),
        ('venta_paga', 'Venta por Paga'),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    tipo_cliente = models.CharField(
        max_length=20,
        choices=TIPOS_CLIENTE,
        default='venta_paga',  # Puedes cambiar el valor por defecto a 'consignacion' si prefieres
    )

    def __str__(self):
        return self.nombre


# Modelo Pedido
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='pedidos')  # Relación con Producto
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.cantidad * self.precio_unitario

    # Validar que el precio unitario del pedido coincida con el precio del producto
    def save(self, *args, **kwargs):
        if self.precio_unitario != self.producto.precio_unitario:
            raise ValueError("El precio unitario debe coincidir con el precio del producto")
        super().save(*args, **kwargs)

    # Método para obtener la URL de detalle del pedido
    def get_absolute_url(self):
        return reverse('pedido_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Pedido de {self.producto.nombre} - Cliente: {self.cliente.nombre}"



