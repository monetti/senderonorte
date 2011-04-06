from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
import datetime

class Region(models.Model):
    slug = models.SlugField(editable=False)
    name = models.CharField(_("Nombre"),max_length="200")
    description = models.TextField(_("Descripcion"))
    def save(self):
        self.slug = slugify(self.name)
        super(Region, self).save()
        
    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regiones')

    def __unicode__(self):
        return self.name
    
class Excurtion(models.Model):
    name = models.CharField(_("Nombre"),max_length="200")
    description = models.TextField(_("Descripcion"))
    summary = models.TextField(_("Resumen"))
    region = models.ForeignKey('Region')
    date = models.DateField(_("Proxima Fecha"))
    place = models.CharField(_('Lugar'),max_length="200")
    time = models.CharField(_('Horario'),max_length="200")
    duration = models.CharField(_("Duracion"),max_length="10")
    publish_last_exc = models.BooleanField(_("Publicar en Ultimas Excursiones?"), default=False,blank=True)
    intro_last_exc = models.TextField(_('Descripcion de la experiencia'),blank=True)
    publish_newsletter = models.BooleanField(_("Publicar en NewsLetter"), default=False,blank=True) 

    class Meta:
        ordering = ('date',)
        verbose_name = _('Excursion')
        verbose_name_plural = _('Listado de Excursiones')
        get_latest_by = 'date'
        
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return u'/excurtion_detail/%s/excurtion' % self.id

       
class PhotoPostExcurtion(models.Model):
    excurtion = models.ForeignKey(Excurtion)
    photo = models.ImageField(upload_to="excurtion", )

    class Meta:
        ordering = ('excurtion',)
        verbose_name = _('Foto Post Excursion')
        verbose_name_plural = _('Listado de Fotos Post Excursion')
        get_latest_by = 'excurtion'
        
    def __unicode__(self):
        return self.photo.name
        
class NextExcurtionFeed(Feed):
    title = "Sendero Norte - Noticias"
    description = "Noticias de Sendero Norte Expediciones"
    link="http://www.senderonorte.com.ar/next-excurtions/feed"
        
    def items(self):
        return Excurtion.objects.all().order_by('-date')[:2]
    
    def item_title(self, item):
        return item.name
    
    def item_link(self,item):
        return "http://senderonorte.com.ar/next-excurtions/feed/detail/"+str(item.id)

    def item_description(self, item):
        return item.description
        

