from django.urls import path
from .views import (
    ClienteListView, ClienteDetailView, ClienteCreateView,
    ClienteUpdateView, ClienteDeleteView, PedidoCreateView, PedidoListView,
    PedidoDetailView, PedidoUpdateView, PedidoDeleteView
)

urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # URLs para pedidos
    path('pedidos/', PedidoListView.as_view(), name='pedido_list'),
    path('pedidos/nuevo/', PedidoCreateView.as_view(), name='pedido_create'),
    path('pedidos/<int:pk>/', PedidoDetailView.as_view(), name='pedido_detail'),  # Agrega esta URL
    path('pedido/<int:pk>/editar/', PedidoUpdateView.as_view(), name='pedido_update'),
    path('pedidos/<int:pk>/eliminar/', PedidoDeleteView.as_view(), name='pedido_delete'),
]
