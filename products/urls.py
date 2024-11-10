from django.urls import path
from .views import FlanView, GelatinasDeMostradorView, GelatinaDeMosaicoView, ProductoListView, ProductoDetailView, AddToCartView, CartDetailView, RemoveFromCartView  # Asegúrate de importar la vista

urlpatterns = [
    path('flan/', FlanView.as_view(), name='flan'),
    path('gelatinas_de_mostrador/', GelatinasDeMostradorView.as_view(), name='gelatinas_de_mostrador'),
    path('gelatina_de_mosaico/', GelatinaDeMosaicoView.as_view(), name='gelatina_de_mosaico'),
    path('productos/', ProductoListView.as_view(), name='products_list'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='products_detail'),
    path('agregar/<int:producto_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('eliminar/<int:producto_id>/', RemoveFromCartView.as_view(), name='eliminar_del_carrito'),  # Aquí agregas la ruta
    path('carrito/', CartDetailView.as_view(), name='cart_detail'),
]