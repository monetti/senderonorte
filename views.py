from django.views.generic import simple
from excurtion.models import Excurtion
from datetime import datetime

def index(request):
    object_list = Excurtion.objects.all()
    incoming = object_list.filter(next_date__gte=datetime.now())[:3]
    recent = object_list.filter(next_date__lt=datetime.now(), published_last_exc=True)[:2]
    
    return simple.direct_to_template(
        request,
        'index.html',
        extra_context = {
            'object_list': object_list,
            'incoming_excurtions': incoming,
            'recent_excurtions': recent,
        }
    )


