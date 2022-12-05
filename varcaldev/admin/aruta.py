#
# Imports :
#
from django.contrib import admin
from varcaldev.models.mruta import *
#
#  name: class Ruta Admin
#
class RutaAdmin(admin.ModelAdmin):
    list_display = (
        'id_ruta',
        'nombre',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['nombre']
    empty_value_display = '-empty-'
admin.site.register(Ruta, RutaAdmin)