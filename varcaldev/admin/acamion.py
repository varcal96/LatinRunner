#
# Imports :
#
from django.contrib import admin
from varcaldev.models.mcamion import *
#
#  name: class Camion Admin
#
class CamionAdmin(admin.ModelAdmin):
    list_display = (
        'id_camion',
        'nombre',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['nombre']
    empty_value_display = '-empty-'
admin.site.register(Camion, CamionAdmin)