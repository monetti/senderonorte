from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template
from django.conf import settings 


admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', 'senderonorte.views.index' , {}, 'home'),
    (r'^acerca_de/', direct_to_template, {'template':'about.html'}),
    (r'^cimblings/', direct_to_template, {'template':'escalada.html'}),
    (r'^educationtravel/', direct_to_template, {'template':'educativos.html'}),
    (r'^customizedtours/', direct_to_template, {'template':'amedida.html'}),
    (r'^recomendations/', direct_to_template, {'template':'recomendaciones.html'}),    
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
