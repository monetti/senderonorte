from django.views.generic import simple, list_detail
from excurtion.models import Excurtion
from excurtion.models import PhotoPostExcurtion
from news.models import New
from cimblings.models import Cimbling
from customizedtravels.models import CustomizedTravel
from educationtravels.models import EducationTravel
from contacts.forms import ContactoForm
from datetime import datetime

def index(request):
    object_list = Excurtion.objects.all()
    incoming = object_list.filter(date__gte=datetime.now()).reverse()[:3]
    recent = object_list.filter(date__lt=datetime.now(), publish_last_exc=True)[:2]
    news = New.objects.all()
    news_news = news.order_by('created_date').reverse()[:3]
    
    return simple.direct_to_template(
        request,
        'index.html',
        extra_context = {
            'object_list': object_list,
            'incoming': incoming,
            'recent_excurtions': recent,
            'news':news_news,
        }
    )
    
def excurtion_detail(request, tag=None,type_object=None):
    excurtion = Excurtion.objects.get(pk=int(tag))
    
    return simple.direct_to_template(
        request,
        'object_detail.html',
        extra_context = {
            'object':excurtion,
            'type_object':type_object,
        }
    )
    
def excurtions(request,tag="norte"):
    excurtions = Excurtion.objects.all()
    norte = excurtions.filter(region__name="norte")[:4]
    patagonia = excurtions.filter(region__name="patagonia")[:4]
    centro = excurtions.filter(region__name="centro")[:4]
    cuyo = excurtions.filter(region__name="cuyo")[:4]
    litoral = excurtions.filter(region__name="litoral")[:4]
    return simple.direct_to_template(
        request,
        'excurtions.html',
        extra_context = {
            'selected':tag,
            'norte':norte,
            'patagonia':patagonia,
            'litoral':litoral,
            'centro':centro,
            'cuyo':cuyo,
        }
    )
    
def cimblings(request):
    cimblings = Cimbling.objects.all()[:4]
    return simple.direct_to_template(
        request,
        'escalada.html',
        extra_context = {
            'cimblings':cimblings,
        }
    )
    
def customizedtravels(request):
    ctravels = CustomizedTravel.objects.all()[:4]
    return simple.direct_to_template(
        request,
        'amedida.html',
        extra_context = {
            'ctravels':ctravels,
        }
    )
    
def educationtravels(request):
    etravels = EducationTravel.objects.all()[:4]
    return simple.direct_to_template(
        request,
        'educativos.html',
        extra_context = {
            'etravels':etravels,
        }
    )
    

def contact(request):
    if request.method == 'POST':
        # peticion POST con formulario relleno
        form = ContactoForm()
        if form.is_valid():
            return simple.direct_to_template(
                request,
                'contacto.html',
                extra_context = {
                    'form':form,
                }
            )
    else: # formulario sin rellenar
        form = ContactoForm()
    return simple.direct_to_template(
        request,
        'contacto.html',
        extra_context = {
              'form': form, 
        }
    )

def contact_sendmail(request):
    import sys
    from smtplib import SMTP

    from_addr = request.POST['email']
    to_addrs = ['contacto@senderonorte.com.ar']
    #msg = open('email_msg.txt','r').read()
    msg = ""
    msg += "Nombre: " + request.POST['nombre'] + "\n"
    msg += "Apellido: " + request.POST['apellido'] + "\n"
    msg += "Email: " + request.POST['email'] + "\n"
    msg += "Excursion: " + request.POST['nombre_excursion'] + ' ' + "Fecha: " + request.POST['fecha'] + "\n"
    msg += "Comentario: " + request.POST['comentario'] + "\n"
    
    
    s = SMTP('smtp.webfaction.com')
    s.login('senderonorte','10a1d322')
    s.sendmail(from_addr, to_addrs, msg)
    return contact(request)


def feed_next_excurtion():
    pass
    
def calendar(request):

    queryset = Excurtion.objects.all() 
    return list_detail.object_list(
        request,
        queryset,
        template_name='calendar.html',
    )
    

