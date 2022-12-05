#
# Imports :
#
from django import forms
from django.forms import ModelForm
from django.forms import Textarea, CharField, TextInput, ChoiceField, Select, NumberInput
from varcaldev.models.mcliente import Cliente
#
#  name: class clienteForm
#
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['id_cliente', 'tipo_persona', 'nombre', 'celular', 'telefono', 'origen']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['id_cliente'].label = "Cédula / RIF del Cliente"
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
