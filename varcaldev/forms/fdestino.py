#
# Imports :
#
from django import forms
from django.forms import ModelForm
from django.forms import Textarea, CharField, TextInput, ChoiceField, Select, NumberInput
from varcaldev.models.mdestino import Destino
#
#  name: class DestinoForm
#
class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ['id_destino', 'nombre', 'rutas']

    def __init__(self, *args, **kwargs):
        super(DestinoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })