from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
#
from varcaldev.urls_views import *
#
urlpatterns = [
   path('', include(ubase)),
   path('', include(udestino)),
   path('', include(uguia)),
   path('', include(uorigen)),
   path('', include(uruta)),
   path('', include(upaquetes)),
   path('', include(ucamion)),
   path('', include(ucliente)),
   path('', include(uemails))
]
