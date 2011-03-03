from django.views.generic import simple
from excurtion.models import Excurtion
from excurtion.models import PhotoPostExcurtion
from news.models import New
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
    return simple.direct_to_template(
        request,
        'excurtions.html',
    )
