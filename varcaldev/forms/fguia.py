#
# Imports :
#
from django import forms
from django.forms import ModelForm
from django.forms import Textarea, CharField, TextInput, ChoiceField, Select, NumberInput
from varcaldev.models.mguia import Guia
from varcaldev.models.mcliente import Cliente
from varcaldev.models.morigen import Origen
from varcaldev.models.musersuc import USucursal
from varcaldev.models.mdestino import Destino
from varcaldev.models.mruta import Ruta
import json
#
#  name: class GuiaForm
#
class GuiaForm(forms.ModelForm):
    class Meta:
        model = Guia
        fields = ['guia', 'recolecta', 'cantidad', 'origen', 'ruta', 'remitente', 'email_r', 'destinatario', 'email_d', 'destino']
        widgets = {
            'remitente': Select(attrs={'id':'remitente'}),
            'email_r': Select(attrs={'id':'email_r'}),
            'email_d': Select(attrs={'id':'email_d'}),
            'destinatario': Select(attrs={'id':'destinatario'})
        }
        
    def __init__(self, *args, **kwargs):
        super(GuiaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['errors'] = form.errors
                #print('error' + data)
        except Exception as e:
            data['errors'] = str(e)
        return data

#
#  name: class GuiaForm
#
class GuiaDForm(forms.ModelForm):
    class Meta:
        model = Guia
        fields = ['guia', 'recolecta', 'cantidad', 'origen', 'ruta', 'remitente', 'destinatario', 'destino']
    def __init__(self, *args, **kwargs):
        super(GuiaDForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })