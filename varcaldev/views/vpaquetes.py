#
# Imports :
#
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic import View
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from varcaldev.models.mpaquetes import *
from varcaldev.models.mcamion import *
from varcaldev.models.mcliente import *
#
#  name: function cargar
#
def cargar(request):
    object_list = Camion.objects.all()
    context = {
        'object_list' : object_list,
    }
    return render(request, "paquete/c_.html", context)
#
#  name: function cargar
#
def descargar(request):
    return render(request, "paquete/d_.html")
#
#  name: function cargar
#
def entregar(request):
    return render(request, "paquete/e_.html")
#
#  name: CargarCamion 
#
class CargarCamion(SuccessMessageMixin, View):
    model = Paquete
    def get(self, request, *args, **kwargs):
        today = str(datetime.now())
        query = self.request.GET.get("q")
        var_camion = self.request.GET.get("camion")
        try:
            query_a = Paquete.objects.filter(id_paquete__icontains=query)
            valor_0 = query_a[0].estado 
            var_guia = query_a[0].guias
            query_m = Guia.objects.filter(guia__exact=var_guia)
            cantidad_guia = query_m[0].cantidad
            if valor_0 == '0':
                if int(cantidad_guia) <= 50:
                    Paquete.objects.filter(id_paquete__icontains=query).update(estado="1", camion=var_camion, modified=today)
                else:
                    Paquete.objects.filter(guias__exact=var_guia).update(estado="1", camion=var_camion, modified=today)
                count_Paquetes = CountPaquetes(num_guia=var_guia, estado="0")
                if count_Paquetes == 0:
                    if ValFirstMail(num_guia=var_guia):
                        pass
                    else:
                        query_c = Guia.objects.filter(guia__exact=var_guia)
                        correo_r = query_c[0].email_r
                        SendCorreo(sndemail=correo_r, msjhtml='Su envío se encuentra en ruta de transito.')
                        correo_d = query_c[0].email_d
                        SendCorreo(sndemail=correo_d, msjhtml='Su envío se encuentra en ruta de transito.')
                        Guia.objects.filter(guia__exact=var_guia).update(fmail=True)
                success_message = "Paquete cargado Correctamente!"
                return HttpResponseRedirect(self.get_success_url(success_message))
            else:  
                if ValFirstMail(num_guia=var_guia):
                    pass
                else:
                    query_c = Guia.objects.filter(guia__exact=var_guia)
                    correo_r = query_c[0].email_r
                    SendCorreo(sndemail=correo_r, msjhtml='Su envío se encuentra en ruta de transito.')
                    correo_d = query_c[0].email_d
                    SendCorreo(sndemail=correo_d, msjhtml='Su envío se encuentra en ruta de transito.')
                    Guia.objects.filter(guia__exact=var_guia).update(fmail=True)
                success_message = "El Paquete ya fue cargado Correctamente - Escanee otro Código!"
                return HttpResponseRedirect(self.get_success_url(success_message))
        except Exception as e:
            success_message = "Error al cargar el Paquete!!" + str(e)
            return HttpResponseRedirect(self.get_success_url(success_message))
    def get_success_url(self, success_message):
        messages.success(self.request, (success_message))
        return reverse("cargar")
#
#  name: DescargarCamion 
#
class DescargarCamion(SuccessMessageMixin, View):
    model = Paquete
    def get(self, request, *args, **kwargs):
        today = str(datetime.now())
        query = self.request.GET.get("q")
        try:
            query_a = Paquete.objects.filter(id_paquete__icontains=query)
            valor_0 = query_a[0].estado
            var_guia = query_a[0].guias
            query_m = Guia.objects.filter(guia__exact=var_guia)
            cantidad_guia = query_m[0].cantidad
            if valor_0 == '1':
                if int(cantidad_guia) <= 50:
                    Paquete.objects.filter(id_paquete__icontains=query).update(estado="2", modified=today)
                else:
                    Paquete.objects.filter(guias__exact=var_guia).update(estado="2", modified=today)
                count_Paquetes = CountPaquetes(num_guia=var_guia, estado="1")
                if count_Paquetes == 0:
                    if ValSecondMail(num_guia=var_guia):
                        pass
                    else:
                        query_c = Guia.objects.filter(guia__exact=var_guia)
                        correo_r = query_c[0].email_r
                        SendCorreo(sndemail=correo_r, msjhtml='Su envío se encuentra en proceso de entrega en la ciudad de destino.')
                        correo_d = query_c[0].email_d
                        SendCorreo(sndemail=correo_d, msjhtml='Su envío se encuentra en proceso de entrega en la ciudad de destino.')
                        Guia.objects.filter(guia__exact=var_guia).update(smail=True)
                success_message = "Paquete descargado Correctamente!"
                return HttpResponseRedirect(self.get_success_url(success_message))
            else:  
                if ValSecondMail(num_guia=var_guia):
                    pass
                else:
                    query_c = Guia.objects.filter(guia__exact=var_guia)
                    correo_r = query_c[0].email_r
                    SendCorreo(sndemail=correo_r, msjhtml='Su envío se encuentra en proceso de entrega en la ciudad de destino.')
                    correo_d = query_c[0].email_d
                    SendCorreo(sndemail=correo_d, msjhtml='Su envío se encuentra en proceso de entrega en la ciudad de destino.')
                    Guia.objects.filter(guia__exact=var_guia).update(smail=True)
                success_message = "El Paquete ya fue descargado Correctamente - Escanee otro Código!"
                return HttpResponseRedirect(self.get_success_url(success_message))
        except Exception as e:
            success_message = "Error al descargar el Paquete!!" + str(e)
            return HttpResponseRedirect(self.get_success_url(success_message))
    def get_success_url(self, success_message):
        messages.success(self.request, (success_message))
        return reverse("descargar")
#
#  name: EntregarPaquete 
#
class EntregarPaquete(SuccessMessageMixin, View):
    model = Paquete
    def get(self, request, *args, **kwargs):
        today = str(datetime.now())
        query = self.request.GET.get("q")
        try:
            query_a = Paquete.objects.filter(id_paquete__icontains=query)
            valor_0 = query_a[0].estado
            var_guia = query_a[0].guias
            query_m = Guia.objects.filter(guia__exact=var_guia)
            cantidad_guia = query_m[0].cantidad
            if valor_0 == '2':
                if int(cantidad_guia) <= 50:
                    Paquete.objects.filter(id_paquete__icontains=query).update(estado="3", modified=today)
                else:
                    Paquete.objects.filter(guias__exact=var_guia).update(estado="3", modified=today)
                count_Paquetes = CountPaquetes(num_guia=var_guia, estado="2")
                if count_Paquetes == 0:
                    if ValThirdMail(num_guia=var_guia):
                        pass
                    else:
                        query_c = Guia.objects.filter(guia__exact=var_guia)
                        correo_r = query_c[0].email_r
                        SendCorreo(sndemail=correo_r, msjhtml='Su envío fue entregado al Cliente.')
                        Guia.objects.filter(guia__exact=var_guia).update(tmail=True)
                        Guia.objects.filter(guia__exact=var_guia).update(estado="I")
                success_message = "Paquete entregado Correctamente!"
                return HttpResponseRedirect(self.get_success_url(success_message))
            else:
                if ValThirdMail(num_guia=var_guia):
                    pass
                else:
                    query_c = Guia.objects.filter(guia__exact=var_guia)
                    correo_r = query_c[0].email_r
                    SendCorreo(sndemail=correo_r, msjhtml='Su envío fue entregado al Cliente.')
                    Guia.objects.filter(guia__exact=var_guia).update(tmail=True)
                    Guia.objects.filter(guia__exact=var_guia).update(estado="I")
                success_message = "El Paquete ya fue entregado Correctamente - Escanee otro Código!"
                return HttpResponseRedirect(self.get_success_url(success_message))
        except Exception as e:
            success_message = "Error al entregar el Paquete!!" + str(e)
            return HttpResponseRedirect(self.get_success_url(success_message))
    def get_success_url(self, success_message):
        messages.success(self.request, (success_message))
        return reverse("entregar")
#
# Function : SendCorreo
#
def SendCorreo(sndemail, msjhtml):
    try:
        email = sndemail
        message = MIMEMultipart('alternative')
        message['Subject'] = 'Notificación de su envío por FLETES GAG'
        message['From'] = settings.EMAIL_HOST_USER
        message['To'] = email
        html = msjhtml
        content = MIMEText(html, 'plain')
        message.attach(content)
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.starttls()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(
            settings.EMAIL_HOST_USER, email, message.as_string()
        )
        server.quit()
    except Exception as e:
        print(str(e))
#
# Function : ValFirstMail
#
def ValFirstMail(num_guia):
    query = Guia.objects.filter(guia__exact=num_guia)
    val_fmail = query[0].fmail
    if val_fmail == True:
        return True
    else:
        return False
#
# Function : ValSecondMail
#
def ValSecondMail(num_guia):
    query = Guia.objects.filter(guia__exact=num_guia)
    val_smail = query[0].smail
    if val_smail == True:
        return True
    else:
        return False
#
# Function : ValThirdMail
#
def ValThirdMail(num_guia):
    query = Guia.objects.filter(guia__exact=num_guia)
    val_tmail = query[0].tmail
    if val_tmail == True:
        return True
    else:
        return False
#
# Function : CountPaquetes
#
def CountPaquetes(num_guia, estado):
    query = Paquete.objects.filter(Q(guias__icontains=num_guia) & Q(estado=estado))
    total = query.count()
    return total