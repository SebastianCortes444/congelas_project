from django.db import models


class ContactMessage(models.Model):
    # Definir las opciones para el tipo de pedido
    EVENTO = 'EV'
    TIENDA = 'TI'
    RESTAURANTE = 'RE'

    PEDIDO_OPCIONES = [
        (EVENTO, 'Evento'),
        (TIENDA, 'Tienda'),
        (RESTAURANTE, 'Restaurante'),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True)  # Opcional
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    # Nuevo campo para el tipo de pedido
    tipo_pedido = models.CharField(
        max_length=2,
        choices=PEDIDO_OPCIONES,
        default=EVENTO,  # Se puede ajustar el valor predeterminado
    )

    # Nuevos campos para la ubicación
    estado = models.CharField(max_length=100)  # Estado o provincia
    municipio = models.CharField(max_length=100)  # Municipio o ciudad

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.email} ({self.get_tipo_pedido_display()}) - {self.municipio}, {self.estado}"
