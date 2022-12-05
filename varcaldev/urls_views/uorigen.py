#
# Imports :
#
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from varcaldev.views.vorigen import *

urlpatterns = [
    path("origen/", login_required(Listado.as_view()), name="l_Origen"),
    path("origen/crear", login_required(Crear.as_view()), name="c_Origen"),
    path("origen/detalle/<str:pk>", login_required(Detalle.as_view()), name="d_Origen"),
    path("origen/actualizar/<str:pk>", login_required(Actualizar.as_view()), name="u_Origen"),
    path("origen/eliminar/<str:pk>", login_required(Eliminar.as_view()), name="e_Origen"),
    path("origen/search", login_required(SearchResultsView.as_view()), name="s_Origen"),
    path("origen/pdf/", login_required(GeneratePdfList.as_view()), name="pl_Origen"),
    path("origen/pdf/<str:pk>", login_required(GeneratePdfUnid.as_view()), name="pu_Origen")
]