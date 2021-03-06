from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import simple, list_detail
from django.http import Http404
from excurtion.models import Excurtion
from excurtion.models import PhotoPostExcurtion
from news.models import New
from cimblings.models import Cimbling
from customizedtravels.models import CustomizedTravel
from educationtravels.models import EducationTravel
from contacts.forms import ContactoForm
from contacts.models import ContactGroup
from datetime import datetime
from activities.models import Activitie
from userprofile.models import UserProfile, Logo
import time
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from forms import UploadFileForm

from models import Video

def index(request):
    object_list = Excurtion.objects.all()
    incoming = object_list.filter(date__gte=datetime.now())[:10]
    recent = object_list.filter(date__lt=datetime.now(), publish_last_exc=True)[:6]
    news_news = New.objects.all()[:1]
    list_videos = Video.objects.all()[:1]
    
    return simple.direct_to_template(
        request,
        'index.html',
        extra_context = {
            'object_list': object_list,
            'incoming': incoming,
            'recent_excurtions': recent,
            'news':news_news,
            'list_videos':list_videos,
        }
    )

def activitie_detail(request,id):
    obj = Activitie.objects.get(pk=int(id))
    
    next_excurtion = Excurtion.objects.filter(activitie=obj.id,date__gte=datetime.now())
    if len(next_excurtion)>0:
        next_excurtion = next_excurtion[0]
    else:
        next_excurtion = None
        
    return simple.direct_to_template(
        request,
        'activitie_detail.html',
        extra_context = {
            'object':obj,
            'next_excurtion':next_excurtion,
        }
    )

#def new_detail(request,id):
#    obj = New.objects.get(pk=int(id))
#    
#    return simple.direct_to_template(
#        request,
#        'new_detail.html',
#        extra_context = {
#            'object':obj,
#        }
#    )

def excurtion_detail(request, tag=None,type_object=None):
    obj = {}
    klass = {
        'excurtion': Excurtion,
        'new': New,
        'ctravel': CustomizedTravel,
        'cimbling': Cimbling,
        'etravel': EducationTravel,
        'user': UserProfile,
    }
    if type_object is not None:
        obj = get_object_or_404(klass[type_object], pk=int(tag))
        return simple.direct_to_template(
            request,
            'object_detail.html',
            extra_context = {
                'object':obj,
                'type_object':type_object,
            }
        )
    else:
        raise Http404
    
def lastexcurtion_detail(request, id):
    obj = Excurtion.objects.get(pk=int(id))
      
    return simple.direct_to_template(
        request,
        'lastexcurtion_detail.html',
        extra_context = {
            'object':obj,
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

    from_addr = request.POST.get('email')
    to_addrs = ['onetti.martin@gmail.com']
    #msg = open('email_msg.txt','r').read()
    msg = ""
    msg += "Nombre: " + unicode(request.POST.get('nombre')) + "\n"
    msg += "Apellido: " + unicode(request.POST.get('apellido')) + "\n"
    msg += "Email: " + unicode(request.POST.get('email')) + "\n"
    msg += "Excursion: " + unicode(request.POST.get('nombre_excursion')) + ' ' + "Fecha: " + unicode(request.POST.get('fecha')) + "\n"
    msg += "Comentario: " + unicode(request.POST.get('comentario')) + "\n"
    
    
    s = SMTP()
    s.connect('smtp.webfaction.com')
    s.login('senderonorte','s3nd3r0n0rt3')
    s.sendmail(from_addr, to_addrs, msg)
    return contact(request)


def feed_next_excurtion():
    pass
    
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

    from contacts.models import Contact, ContactGroup

    grupos = ContactGroup.objects.all()

    if request.method == "POST":
        if 'file' in request.FILES:
            import xlrd
            
            from django.conf import settings

            file = request.FILES['file']
            
            wb = xlrd.open_workbook(file_contents=file.read())
            sh = wb.sheet_by_index(0)

            for rownum in range(1,sh.nrows):
                row = sh.row_values(rownum)           
                ctc = Contact()
                ctc.name = row[0]
                ctc.last_name = row[1]
                ctc.email = row[2]
                ctc.grupo = ContactGroup.objects.get(pk=row[3])
                ctc.save()
 
    form = UploadFileForm()
    
    return simple.direct_to_template(
        request,
        'issues.html',
        extra_context = {
            'grupos':grupos,
            'formMass':form,
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

    if request.method == 'POST':
        heading = request.POST['title_newsletter']
    else:
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

    msg.send()
    
    return issues(request)

def us_page(request):
    staff = UserProfile.objects.all()
    logos = Logo.objects.all()
    return simple.direct_to_template(
        request,
        'nosotros.html',
        extra_context = {
            'staff':staff,
            'logos':logos,
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
    
def refugios(request):
    return render_to_response("refugios.html", {})
