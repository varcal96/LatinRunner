#
# Imports :
#
from django.contrib import admin
from varcaldev.models.mpaquetes import *
#
#  name: class Bultos Admin
#
class BultoAdmin(admin.ModelAdmin):
    list_display = (
        'id_bulto',
        'guias',
        'recolecta',
        'estado',
        'origen',
        'ruta',
        'destino',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['guias']
    empty_value_display = '-empty-'
admin.site.register(Paquete, BultoAdmin)