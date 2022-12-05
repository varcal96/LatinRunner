#
# Imports :
#
from django import forms
from django.forms import ModelForm
from django.forms import Textarea, CharField, TextInput, ChoiceField, Select, NumberInput
from varcaldev.models.morigen import Origen
#
#  name: class OrigenForm
#
class OrigenForm(forms.ModelForm):
    class Meta:
        model = Origen
        fields = ['id_origen', 'nombre']

    def __init__(self, *args, **kwargs):
        super(OrigenForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })