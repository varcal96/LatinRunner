#
# Imports :
#
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from varcaldev.views.vbase import *

urlpatterns = [
    path('', index, name='index'),
    path('home', login_required(home), name='home'),
    path('search', SearchResultsView.as_view(), name="s_Bulto"),
]