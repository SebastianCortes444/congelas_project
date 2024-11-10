from .views import HomePageView, SobreNosotrosView, PreguntasFrecuentesView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('sobre_nosotros/', SobreNosotrosView.as_view(), name='sobre_nosotros'),
    path('preguntas_frecuentes', PreguntasFrecuentesView.as_view(), name='preguntas_frecuentes')
]