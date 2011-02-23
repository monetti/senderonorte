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
            'incoming_one': incoming[0],
            'incoming_two':incoming[1],
            'incoming_three':incoming[2],            
            'recent_excurtions': recent,
            'news':news_news,
        }
    )


