#
# Imports :
#
from django.contrib import admin
from varcaldev.models.mguia import *
#
#  name: class Guia Admin
#
class GuiaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'guia',
        'recolecta',
        'estado',
        'cantidad',
        'remitente',
        'destinatario',
        'ruta',
        'origen',
        'destino',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['id']
    empty_value_display = '-empty-'
admin.site.register(Guia, GuiaAdmin)