from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import TipoUsuario
from .models import Paquete, Cliente
from django_select2.forms import ModelSelect2Widget

class CustomUserCreationForm(UserCreationForm):
    
     # Campos adicionales
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=20)
    tipo_usuario_queryset = TipoUsuario.objects.all()
    tipo_usuario = forms.ModelChoiceField(queryset=tipo_usuario_queryset, empty_label=None)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Agrega la clase 'form-control' a todos los widgets para mantener el estilo de Bootstrap
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''  # Oculta los textos de ayuda
            field.label_classes = ['label-register']

        # Agrega el botón al final del formulario
        self.fields['registrar_button'] = forms.CharField(
            label='',
            widget=forms.TextInput(attrs={'type': 'submit', 'class': 'btn btn-outline-warning', 'value': 'Registrar'})
        )
        
class PaqueteForm(forms.ModelForm):  
    class Meta:
        model = Paquete
        fields = ['peso', 'dimensiones', 'direccion_origen', 'direccion_destino']