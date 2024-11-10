from decimal import Decimal
from django.conf import settings
from .models import Producto

class Carrito:
    def __init__(self, request):
        """
        Inicializa el carrito de compras
        """
        self.session = request.session
        carrito = self.session.get(settings.CART_SESSION_ID)
        if not carrito:
            # Guarda un carrito vacío en la sesión
            carrito = self.session[settings.CART_SESSION_ID] = {}
        self.carrito = carrito

    def add(self, producto, cantidad=1, override_quantity=False):
        """
        Agrega un producto al carrito o actualiza su cantidad.
        """
        producto_id = str(producto.id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {
                'cantidad': 0,
                'precio': str(producto.precio)
            }
        if override_quantity:
            self.carrito[producto_id]['cantidad'] = cantidad
        else:
            self.carrito[producto_id]['cantidad'] += cantidad
        self.save()

    def save(self):
        # Marca la sesión como modificada para asegurar que se guarde
        self.session.modified = True

    def remove(self, producto):
        """
        Elimina un producto del carrito.
        """
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.save()

    def __iter__(self):
        """
        Itera sobre los productos en el carrito y obtiene los productos de la base de datos.
        """
        producto_ids = self.carrito.keys()
        productos = Producto.objects.filter(id__in=producto_ids)
        carrito = self.carrito.copy()

        for producto in productos:
            carrito[str(producto.id)]['producto'] = producto

        for item in carrito.values():
            item['precio'] = Decimal(item['precio'])
            item['total'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        """
        Cuenta todos los productos en el carrito.
        """
        return sum(item['cantidad'] for item in self.carrito.values())

    def get_total_precio(self):
        """
        Obtiene el precio total de los productos en el carrito.
        """
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carrito.values())

    def clear(self):
        """
        Limpia el carrito de la sesión.
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()
