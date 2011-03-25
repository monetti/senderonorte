from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template
from django.conf import settings 
from excurtion.models import NextExcurtionFeed

admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', 'senderonorte.views.index' , {}, 'home'),
    (r'^acerca_de/$', direct_to_template, {'template':'about.html'}),
    (r'^cimblings/$', 'senderonorte.views.cimblings'),
    (r'^educationtravel/$', 'senderonorte.views.educationtravels'),
    (r'^customizedtours/$', 'senderonorte.views.customizedtravels'),
    (r'^recomendations/$', direct_to_template, {'template':'recomendaciones.html'}),    
    (r'^excurtion_detail/(?P<tag>[^/]+)/(?P<type_object>[^/]+)$', 'senderonorte.views.excurtion_detail'),    
    (r'^excurtions/(?P<tag>[^/]+)$', 'senderonorte.views.excurtions'),    
    (r'^contact/$', 'senderonorte.views.contact'),    
    (r'^contact/send$', 'senderonorte.views.contact_sendmail'),        
    (r'^next-excurtions/feed/$', NextExcurtionFeed()),
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
