from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template
from django.conf import settings 

from excurtion.models import Excurtion 

admin.autodiscover()

info = {
    'template':'index.html',
}

info_2 = {
    'queryset':Excurtion.objects.all(),
    'paginate_by':1,
    'page':1,
}

urlpatterns = patterns('',
    (r'^$', 'senderonorte.views.index' , {}, 'home'),
    (r'^acerca_de/', direct_to_template, {'template':'about.html'}),

    #(r'^home/', list_detail.object_list, info_2),
)

urlpatterns += patterns( '',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
     {'document_root': settings.MEDIA_ROOT}),
    )
