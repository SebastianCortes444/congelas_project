from django.urls import path
from .views import ContactFormView, ContactThanksView

urlpatterns = [
    path('contacto/', ContactFormView.as_view(), name='contacto'),
    path('registrado', ContactThanksView.as_view(), name='registrado'),
]
