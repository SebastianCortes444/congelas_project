from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView
from django.contrib import messages
from .forms import ContactForm


class ContactFormView(FormView):
    template_name = 'contact/contact.html'  # El template donde se mostrará el formulario
    form_class = ContactForm  # El formulario definido anteriormente
    success_url = reverse_lazy('registrado')  # Redirige después de un envío exitoso

    def form_valid(self, form):
        # Guarda el formulario si es válido
        form.save()

        # Muestra un mensaje de éxito
        messages.success(self.request, '¡Gracias por contactarnos! Nos pondremos en contacto contigo pronto.')

        # Llama al método por defecto para manejar el redireccionamiento
        return super().form_valid(form)


# Vista para la página de agradecimiento
class ContactThanksView(TemplateView):
    template_name = 'contact/contact_thanks.html'



