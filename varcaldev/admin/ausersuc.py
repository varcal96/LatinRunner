#
# Imports :
#
from django.contrib import admin
from varcaldev.models.musersuc import *
#
#  name: class USucursal Admin
#
class USucursalAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'sucursal',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
admin.site.register(USucursal, USucursalAdmin)