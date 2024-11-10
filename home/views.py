from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView

class HomePageView(TemplateView):
    """home page view"""
    template_name = "home/home.html"

class SobreNosotrosView(TemplateView):
    """About us"""
    template_name = 'us/sobre_nosotros.html'

class PreguntasFrecuentesView(TemplateView):
    """Preguntas frecuentes view"""
    template_name = 'preguntas_frecuentes/preguntas_frecuentes.html'