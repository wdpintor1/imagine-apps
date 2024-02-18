from django import forms
from ..models import Paquete, Cliente

class PaqueteForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), label='Cliente', to_field_name='idCliente')

    class Meta:
        model = Paquete
        fields = ['cliente', 'direccion_origen', 'direccion_destino', 'dimensiones', 'peso']

    def __init__(self, *args, **kwargs):
        super(PaqueteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # Obtén la instancia de Paquete si está presente
        instance = kwargs.get('instance')
        if instance and instance.idCliente:
            # Si hay una instancia de paquete y tiene un cliente asociado,
            # establece ese cliente como el valor seleccionado en el formulario
            self.fields['cliente'].initial = instance.idCliente