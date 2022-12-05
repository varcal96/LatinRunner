#
# Imports :
#
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from varcaldev.views.vpaquetes import *
from varcaldev.views.vbulcarga import *

urlpatterns = [
    path('paquete/carga', login_required(cargar), name='cargar'),
    path("paquete/cargar", login_required(CargarCamion.as_view()), name="c_Bulto"),
    path('paquete/descarga', login_required(descargar), name='descargar'),
    path("paquete/descargar", login_required(DescargarCamion.as_view()), name="d_Bulto"),
    path('paquete/entrega', login_required(entregar), name='entregar'),
    path("paquete/entregar", login_required(EntregarPaquete.as_view()), name="e_Bulto"),
    path('paquete/cargados', login_required(cargados), name='cargados'),
    path("paquete/pdf/", login_required(Paquetesxcargar.as_view()), name="pl_xCargar"),
    path("paquete/pdf1/", login_required(Paquetescargados.as_view()), name="pl_xCargados"),
    path("paquete/pdf2/", login_required(Paquetesxcamion.as_view()), name="pl_xCamion"),
]