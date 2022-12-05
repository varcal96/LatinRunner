#
# Imports :
#
from django.db import models
from crum import get_current_user
from django.utils import timezone
from django.utils.html import format_html
from django.forms import model_to_dict
#
from .morigen import Origen
#
# Class : USucursal
#
class USucursal(models.Model):
    # Usuario
    usuario = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        default=None,
        on_delete=models.DO_NOTHING,
        related_name='usuario',
        verbose_name=u"usuario",
        db_column='usuario')
         # Relacion con Origen
    sucursal = models.ForeignKey(
        Origen,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=u"Sucursal",
        related_name='sucursal_usuario',
        db_column='sucursal')
    # Modificado fecha actual
    modified = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=u"Modificado")
    # Modificado por
    modified_by = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        default=None,
        on_delete=models.DO_NOTHING,
        related_name='usuario_modified_by',
        verbose_name=u"Modificado por",
        db_column='modified_by')
    # Creado campo de fecha automatico fecha actual
    created = models.DateTimeField(auto_now_add=True, verbose_name=u"Creado")
    # Creado por
    created_by = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        default=get_current_user,
        on_delete=models.DO_NOTHING,
        related_name='usuario_create_by',
        verbose_name=u"Creado por",
        db_column='created_by')
    #
    # Colored Fields
    #
    def col_modified(self):
        return format_html(
            '<span style="color: #0091EA;">{0}</span>',
            self.modified
        )
    col_modified.short_description = 'Modificado el'

    def col_modified_by(self):
        return format_html(
            '<span style="color: #F57C00;">{0}</span>',
            self.modified_by
        )
    col_modified_by.short_description = 'Modificado por'

    def col_created(self):
        return format_html(
            '<span style="color: #0091EA;">{0}</span>',
            self.created
        )
    col_created.short_description = 'Creado el'

    def col_created_by(self):
        return format_html(
            '<span style="color: #558B2F;">{0}</span>',
            self.created_by
        )
    col_created_by.short_description = 'Creado por'
    #
    # Save method :
    #
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(USucursal, self).save(*args, **kwargs)
    #
    # Meta and String
    #
    def __str__(self):
        return str(self.sucursal)

    class Meta:
        db_table ='user_sucursal'