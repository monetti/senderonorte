from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import simple, list_detail
from excurtion.models import Excurtion
from excurtion.models import PhotoPostExcurtion
from news.models import New
from cimblings.models import Cimbling
from customizedtravels.models import CustomizedTravel
from educationtravels.models import EducationTravel
from contacts.forms import ContactoForm
from contacts.models import ContactGroup
from gencal.templatetags.gencal import ListCalendar
from datetime import datetime
from activities.models import Activitie
import time
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

def index(request):
    object_list = Excurtion.objects.all()
    incoming = object_list.filter(date__gte=datetime.now())[:10]
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
    obj = {}
    if type_object == "excurtion":
        obj = Excurtion.objects.get(pk=int(tag))
    elif type_object == "new":
         obj = New.objects.get(pk=int(tag))
    elif type_object == "activitie":
        obj = Activitie.objects.get(pk=int(tag))
    else:
        obj = {}
    
    return simple.direct_to_template(
        request,
        'object_detail.html',
        extra_context = {
            'object':obj,
            'type_object':type_object,
        }
    )
    
def excurtions(request,tag="tab-norte"):
    queryset = Activitie.objects.all()
    return list_detail.object_list(
        request,
        queryset,
        template_name='excurtions.html',
        extra_context = {
            'selected':tag
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
    
    from smtplib import SMTP

    from_addr = request.POST['email']
    to_addrs = ['contacto@senderonorte.com.ar']
    #msg = open('email_msg.txt','r').read()
    msg = ""
    msg += "Nombre: " + unicode(request.POST['nombre']) + "\n"
    msg += "Apellido: " + unicode(request.POST['apellido']) + "\n"
    msg += "Email: " + unicode(request.POST['email']) + "\n"
    msg += "Excursion: " + unicode(request.POST['nombre_excursion']) + ' ' + "Fecha: " + unicode(request.POST['fecha']) + "\n"
    msg += "Comentario: " + unicode(request.POST['comentario']) + "\n"
    
    
    s = SMTP()
    s.connect('smtp.webfaction.com')
    s.login('senderonorte','s3nd3r0n0rt3')
    s.sendmail(from_addr, to_addrs, msg)
    return contact(request)


def feed_next_excurtion():
    pass
    
#def calendar(request):
#    queryset = Excurtion.objects.all()
#    return list_detail.object_list(
#        request,
#        queryset,
#        template_name='calendar.html',
#        extra_context = {
#            'list_obj':Excurtion.objects.all(),
#        },
#    )

def feed_detail(request,tag):
    a = Excurtion.objects.get(pk=int(tag))
    if a:
        return simple.direct_to_template(
            request,
            'feed_detail.html',
            extra_context = {
                'obj':a,
            }
        )
    else:
        return simple.direct_to_template(
            request,
            'feed_detail.html',
            extra_context = {
                'obj':{},
            }
        )

def server_error(request):
    return simple.direct_to_template(request, '500.html')

def not_found(request):
    return simple.direct_to_template(request, '404.html')

def test(request):
    return simple.direct_to_template(request, '404.html')


@login_required()
def issues(request):
    grupos = ContactGroup.objects.all()
    
    return simple.direct_to_template(
        request,
        'issues.html',
        extra_context = {
            'grupos':grupos,
        }
    )
    
@login_required()    
def mailing_preview(request):
    excurtions = Excurtion.objects.all().filter(publish_newsletter=True)
    news = New.objects.all().filter(publish_newsletter=True)
    
    return simple.direct_to_template(
        request,
        'plantilla.html',
        extra_context = {
            'excurtions':excurtions,
            'news':news,
        }
    )

@login_required()    
def send_mailing(request):
    from django.template import Context, Template
    from django.template.loader import get_template
    from django.template.loader import render_to_string
    from contacts.models import Contact
    from django.template import loader
    from django.core.mail import send_mail, EmailMultiAlternatives

    import smtplib
    
    excurtions = Excurtion.objects.all().filter(publish_newsletter=True)
    news = New.objects.all().filter(publish_newsletter=True)

    #t = get_template("boletin.html")
    c = Context({"excurtions": excurtions,"news":news})
    #t = render_to_string('boletin.html',{"excurtions": excurtions,"news":news})
    html_part = loader.get_template('%s.html' %("boletin")).render(c)

    msg_mail = []
    heading = '%s' %(':: Sendero Norte :: Boletin de Novedades')
    contacts = []    
    
    groups = ContactGroup.objects.all()
    for g in groups:
        try:
            if request.POST[g.name]:
                contacts = contacts + list(Contact.objects.filter(grupo=g.id))
        except:
            pass
    
    for i in range(0,len(contacts)):    
        msg_mail.append(contacts[i].email)
        
    msg = EmailMultiAlternatives(subject=heading,from_email='contacto@senderonorte.com.ar',bcc=msg_mail,to=['contacto@senderonorte.com.ar'])

    msg.attach_alternative(html_part, "text/html")

    msg.send(False)
    
    return issues(request)

def us_page(request):
    staff = User.objects.filter(is_staff=True)
    return simple.direct_to_template(
        request,
        'nosotros.html',
        extra_context = {
            'staff':staff,
        }
    )


mnames = "Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre"
mnames = mnames.split()


def calendar(request, year=None):
    """Main listing, years and months; three years per page."""
    # prev / next years
    if year: year = int(year)
    else:    year = time.localtime()[0]

    nowy, nowm = time.localtime()[:2]
    lst = []

    # create a list of months for each year, indicating ones that contain entries and current
    for y in [year]:
        mlst = []
        for n, month in enumerate(mnames):
            entry = current = False   # are there entry(s) for this month; current month?
            entries = Excurtion.objects.filter(date__year=y, date__month=n+1)

            if entries:
                entry = True
            if y == nowy and n+1 == nowm:
                current = True
            mlst.append(dict(n=n+1, name=month, entry=entry, current=current,entries=entries))
        lst.append((y, mlst))

    return render_to_response("calendar.html", {'years':lst, 'year':year})
