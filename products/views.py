from django.views.generic import TemplateView, DetailView, ListView
from .models import Producto, ImagenProducto  # Asegúrate de importar ImagenProducto
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from .cart import Carrito

class FlanView(TemplateView):
    template_name = 'products/flan.html'

class GelatinasDeMostradorView(TemplateView):
    template_name = 'products/gelatinas_de_mostrador.html'

class GelatinaDeMosaicoView(TemplateView):
    template_name = 'products/gelatina_de_mosaico.html'

class ProductoListView(ListView):
    model = Producto
    template_name = 'products/products_list.html'  # Ruta al template
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'products/products_detail.html'
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto = self.object  # Obtén el producto actual
        context['imagenes'] = producto.imagenes.all()  # Obtén todas las imágenes del producto
        return context

class AddToCartView(View):
    def post(self, request, producto_id):
        carrito = Carrito(request)
        producto = get_object_or_404(Producto, id=producto_id)
        carrito.add(producto=producto, cantidad=1, override_quantity=False)
        return redirect('cart_detail')

class CartDetailView(TemplateView):
    template_name = 'cart/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carrito = Carrito(self.request)
        context['carrito'] = carrito
        context['total_precio'] = carrito.get_total_precio()
        context['items'] = []  # Para almacenar los productos con sus detalles

        # Obtener detalles de los productos en el carrito
        for item in carrito:
            producto = item['producto']  # Obtener el producto directamente del item
            context['items'].append({
                'producto': producto,
                'cantidad': item['cantidad'],
                'total': producto.precio * item['cantidad']
            })

        return context

class RemoveFromCartView(View):
    def post(self, request, producto_id):
        carrito = Carrito(request)
        producto = get_object_or_404(Producto, id=producto_id)
        carrito.remove(producto)
        return redirect('cart_detail')
