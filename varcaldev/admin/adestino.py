#
# Imports :
#
from django.contrib import admin
from varcaldev.models.mdestino import *
#
#  name: class Destino Admin
#
class DestinoAdmin(admin.ModelAdmin):
    list_display = (
        'id_destino',
        'nombre',
        'rutas',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['nombre']
    empty_value_display = '-empty-'
admin.site.register(Destino, DestinoAdmin)