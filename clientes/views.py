from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Pedido
from .forms import ClienteForm, PedidoForm

from django.contrib.auth.mixins import LoginRequiredMixin


# Vistas para Clientes
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'
    login_url = 'login'

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'
    login_url = 'login'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener los pedidos asociados al cliente
        cliente = self.get_object()
        pedidos = Pedido.objects.filter(cliente=cliente)
        context['pedidos'] = pedidos  # Agregar los pedidos al contexto
        return context

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    login_url = 'login'


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    login_url = 'login'


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
    login_url = 'login'


# Vistas para Pedidos
class PedidoCreateView(LoginRequiredMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'clientes/pedido_form.html'
    login_url = 'login'


    def form_valid(self, form):
        # Guardar el pedido
        response = super().form_valid(form)
        # Redirigir al detalle del cliente después de crear el pedido
        # Usamos reverse_lazy para que Django genere la URL después de la creación del pedido
        self.success_url = reverse_lazy('cliente_detail', kwargs={'pk': form.instance.cliente.pk})
        return response

class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    login_url = 'login'
    template_name = 'clientes/pedido_list.html'  # Plantilla donde se mostrarán los pedidos
    context_object_name = 'pedidos'  # Nombre del contexto para la plantilla

class PedidoDetailView(LoginRequiredMixin, DetailView):
    model = Pedido
    template_name = 'clientes/pedido_detail.html'  # Plantilla de detalle del pedido
    context_object_name = 'pedido'
    login_url = 'login'

class PedidoUpdateView(LoginRequiredMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    login_url = 'login'
    template_name = 'clientes/pedido_update.html'  # Asegúrate de que esta plantilla esté definida
    success_url = reverse_lazy('pedido_list')  # Redirige a la lista de pedidos después de la actualización

class PedidoDeleteView(LoginRequiredMixin, DeleteView):
    model = Pedido
    login_url = 'login'
    template_name = 'clientes/pedido_confirm_delete.html'
    success_url = reverse_lazy('pedido_list')  # Redirige a la lista de pedidos después de eliminar