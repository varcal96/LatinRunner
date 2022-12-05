#
# Imports :
#
from datetime import date, datetime
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from varcaldev.models.mpaquetes import *
from varcaldev.models.morigen import *
#
# Function : Index
#
def index(request):
    object_list = Origen.objects.all()
    context = {
        'object_list' : object_list,
    }
    return render(request, 'index.html', context)
#
# Function : CountPaquetesSucursal
#
def CountPaquetesSucursal(origen, estado):
    today = date.today()
    query = Bulto.objects.filter(Q(origen__icontains=origen) & Q(estado=estado) & Q(modified__contains=today))
    total = query.count()
    return total
#
# Function : CountPaquetesRuta
#
def CountPaquetesRuta(ruta, estado):
    today = date.today()
    query = Bulto.objects.filter(Q(ruta__icontains=ruta) & Q(estado=estado) & Q(modified__contains=today))
    total = query.count()
    return total
#
# Function : CountPaquetesMes
#
def CountPaquetesMes(mes, estado):
    today = date.today()
    #print(today.year)
    query = Bulto.objects.filter(Q(estado=estado) & Q(modified__month=mes) & Q(modified__year=today.year))
    total = query.count()
    return total
#
# Function : CountPaquetesYear
#
def CountPaquetesYear(year, estado):
    query = Bulto.objects.filter(Q(estado=estado) & Q(modified__year=year))
    total = query.count()
    return total
#
# Function : Home DashBoard
#
def home(request):
    model = Bulto
    labels1 = ['BNA', 'BQO', 'CCS', 'COR', 'MIQ', 'MBO', 'MCY', 'POZ', 'PFO', 'SAN', 'VAL']
    TB_BNA = CountPaquetesSucursal(origen="BNA", estado="0")
    TB_BQO = CountPaquetesSucursal(origen="BQO", estado="0")
    TB_CCS = CountPaquetesSucursal(origen="CCS", estado="0")
    TB_COR = CountPaquetesSucursal(origen="COR", estado="0")
    TB_MIQ = CountPaquetesSucursal(origen="MIQ", estado="0")
    TB_MBO = CountPaquetesSucursal(origen="MBO", estado="0")
    TB_MCY = CountPaquetesSucursal(origen="MCY", estado="0")
    TB_POZ = CountPaquetesSucursal(origen="POZ", estado="0")
    TB_PFO = CountPaquetesSucursal(origen="PFO", estado="0")
    TB_SAN = CountPaquetesSucursal(origen="SAN", estado="0")
    TB_VAL = CountPaquetesSucursal(origen="VAL", estado="0")
    data1 = [TB_BNA, TB_BQO, TB_CCS, TB_COR, TB_MIQ, TB_MBO, TB_MCY, TB_POZ, TB_PFO, TB_SAN, TB_VAL]
    
    labels2 = ['BNA','BQO','CCS','COR','LLS','MBO','MCY','MER','MIQ','OCC','OR1','OR2','PFO','POZ','SAN','VAL']
    TB2_BNA = CountPaquetesRuta(ruta="BNA", estado="0")
    TB2_BQO = CountPaquetesRuta(ruta="BQO", estado="0")
    TB2_CCS = CountPaquetesRuta(ruta="CCS", estado="0")
    TB2_COR = CountPaquetesRuta(ruta="COR", estado="0")
    TB2_LLS = CountPaquetesRuta(ruta="LLS", estado="0")
    TB2_MBO = CountPaquetesRuta(ruta="MBO", estado="0")
    TB2_MCY = CountPaquetesRuta(ruta="MCY", estado="0")
    TB2_MER = CountPaquetesRuta(ruta="MER", estado="0")
    TB2_MIQ = CountPaquetesRuta(ruta="MIQ", estado="0")
    TB2_OCC = CountPaquetesRuta(ruta="OCC", estado="0")
    TB2_OR1 = CountPaquetesRuta(ruta="OR1", estado="0")
    TB2_OR2 = CountPaquetesRuta(ruta="OR2", estado="0")
    TB2_PFO = CountPaquetesRuta(ruta="PFO", estado="0")
    TB2_POZ = CountPaquetesRuta(ruta="POZ", estado="0")
    TB2_SAN = CountPaquetesRuta(ruta="SAN", estado="0")
    TB2_VAL = CountPaquetesRuta(ruta="VAL", estado="0")
    data2 = [TB2_BNA, TB2_BQO, TB2_CCS, TB2_COR, TB2_LLS, TB2_MBO, TB2_MCY, TB2_MER, TB2_MIQ, TB2_OCC, TB2_OR1, TB2_OR2, TB2_PFO, TB2_POZ, TB2_SAN, TB2_VAL]
    
    labels3 = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    TB_ENE = CountPaquetesMes(mes="01", estado="0")
    TB_FEB = CountPaquetesMes(mes="02", estado="0")
    TB_MAR = CountPaquetesMes(mes="03", estado="0")
    TB_ABR = CountPaquetesMes(mes="04", estado="0")
    TB_MAY = CountPaquetesMes(mes="05", estado="0")
    TB_JUN = CountPaquetesMes(mes="06", estado="0")
    TB_JUL = CountPaquetesMes(mes="07", estado="0")
    TB_AGO = CountPaquetesMes(mes="08", estado="0")
    TB_SEP = CountPaquetesMes(mes="09", estado="0")
    TB_OCT = CountPaquetesMes(mes="10", estado="0")
    TB_NOV = CountPaquetesMes(mes="11", estado="0")
    TB_DIC = CountPaquetesMes(mes="12", estado="0")
    data3 = [TB_ENE, TB_FEB, TB_MAR, TB_ABR, TB_MAY, TB_JUN, TB_JUL, TB_AGO, TB_SEP, TB_OCT, TB_NOV, TB_DIC]

    today = date.today()
    labels4 = [str(today.year), str(today.year - 1), str(today.year - 2), str(today.year - 3), str(today.year - 4)]
    TB_YA = CountPaquetesYear(year=str(today.year), estado="0")
    TB_LY = CountPaquetesYear(year=str(today.year - 1), estado="0")
    TB_Y3 = CountPaquetesYear(year=str(today.year - 2), estado="0")
    TB_Y4 = CountPaquetesYear(year=str(today.year - 3), estado="0")
    TB_Y5 = CountPaquetesYear(year=str(today.year - 4), estado="0")
    data4 = [TB_YA, TB_LY, TB_Y3, TB_Y4, TB_Y5]
 
    return render(request, 'home.html',  {
        'labels1': labels1,
        'data1': data1,
        'labels2': labels2,
        'data2': data2,
        'labels3': labels3,
        'data3': data3,
        'labels4': labels4,
        'data4': data4,
        })
#
#  name: class SearchResultsView
#
class SearchResultsView(ListView):
    model = Paquete
    template_name = "s_.html"
    def get_queryset(self):
        query_a = self.request.GET.get("origen")
        query_b = self.request.GET.get("q")
        object_list = Paquete.objects.filter(Q(guias__exact=query_b) & Q(origen__contains=query_a)
            | Q(recolecta__exact=query_b) & Q(origen__contains=query_a)
            #Q(guia_id__icontains=query) | Q(id_paquete__icontains=query)
            )
        return object_list
