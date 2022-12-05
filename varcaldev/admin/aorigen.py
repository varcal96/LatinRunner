#
# Imports :
#
from django.contrib import admin
from varcaldev.models.morigen import *
#
#  name: class Origen Admin
#
class OrigenAdmin(admin.ModelAdmin):
    list_display = (
        'id_origen',
        'nombre',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['nombre']
    empty_value_display = '-empty-'
admin.site.register(Origen, OrigenAdmin)