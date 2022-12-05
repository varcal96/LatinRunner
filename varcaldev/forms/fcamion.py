#
# Imports :
#
from django import forms
from django.forms import ModelForm
from django.forms import Textarea, CharField, TextInput, ChoiceField, Select, NumberInput
from varcaldev.models.mcamion import Camion
#
#  name: class CamionForm
#
class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['id_camion', 'nombre']

    def __init__(self, *args, **kwargs):
        super(CamionForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })