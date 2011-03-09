from django.views.generic import simple
from excurtion.models import Excurtion
from excurtion.models import PhotoPostExcurtion
from news.models import New
from cimblings.models import Cimbling
from customizedtravels.models import CustomizedTravel
from educationtravels.models import EducationTravel
from datetime import datetime

def index(request):
    object_list = Excurtion.objects.all()
    incoming = object_list.filter(next_date__gte=datetime.now()).reverse()[:3]
    recent = object_list.filter(next_date__lt=datetime.now(), publish_last_exc=True)[:2]
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
    
def excurtions(request,tag=None):
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
