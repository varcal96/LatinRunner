#
# Imports :
#
from django.contrib import admin
from varcaldev.models.memail import *
#
#  name: class cliente Admin
#
class EmailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_cliente',
        'email',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['id']
    empty_value_display = '-empty-'
admin.site.register(Email, EmailAdmin)