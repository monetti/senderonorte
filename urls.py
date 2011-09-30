from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template
from django.conf import settings 
from excurtion.models import NextExcurtionFeed

admin.autodiscover()

handler500 = 'senderonorte.views.server_error'
handler404 = 'senderonorte.views.not_found'

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
    (r'^next-excurtions/feed/detail/(?P<tag>[^/]+)$', 'senderonorte.views.feed_detail'),

    (r'^us/$', 'senderonorte.views.us_page'),
    (r'^calendar$', 'senderonorte.views.calendar'),

    (r'^activitie_detail/(?P<id>[^/]+)/$', 'senderonorte.views.activitie_detail'),
    (r'^lastexcurtion_detail/(?P<id>[^/]+)/$', 'senderonorte.views.lastexcurtion_detail'),
    
    (r'^mailing/issues/$', 'senderonorte.views.issues'),
    (r'^mailing/send', 'senderonorte.views.send_mailing'),
    (r'^mailing/preview$', 'senderonorte.views.mailing_preview'),
    
    (r'^refugios/$', 'senderonorte.views.refugios'),
)

urlpatterns += patterns('',
    (r'^test/$', 'senderonorte.views.not_found'),
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
