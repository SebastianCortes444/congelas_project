from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nombre', 'email', 'telefono', 'mensaje', 'tipo_pedido', 'estado', 'municipio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu email'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu teléfono (opcional)'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje aquí'}),
            'tipo_pedido': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu estado o provincia'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu municipio o ciudad'}),
        }
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono (Opcional)',
            'mensaje': 'Mensaje',
            'tipo_pedido': 'Tipo de Pedido',
            'estado': 'Estado',
            'municipio': 'Municipio',
        }

