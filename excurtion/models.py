from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.syndication.views import Feed
from thumbs import ImageWithThumbsField
from django.shortcuts import get_object_or_404
    
import datetime

class Region(models.Model):
    name = models.CharField(_("Nombre"),max_length="200")
    description = models.TextField(_("Descripcion"))
    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regiones')

    def __unicode__(self):
        return self.name
    
class Excurtion(models.Model):
    name = models.CharField(_("Nombre"),max_length="200")
    description = models.TextField(_("Descripcion"))
    summary = models.TextField(_("Resumen"))
    date = models.DateField(_("Proxima Fecha"))
    place = models.CharField(_('Lugar'),max_length="200")
    time = models.CharField(_('Horario'),max_length="200")
    duration = models.CharField(_("Duracion"),max_length="10")
    
    foto_carrusel_uno = ImageWithThumbsField(name="photo_carrusel_one",upload_to="./img/excurtion", sizes=((540,340),(280,80),))
    foto_carrusel_dos = ImageWithThumbsField(name="photo_carrusel_two",upload_to="./img/excurtion")
    foto_carrusel_tres = ImageWithThumbsField(name="photo_carrusel_three",upload_to="./img/excurtion")
           
    publish_last_exc = models.BooleanField(_("Publicar en Ultimas Excursiones?"), default=False,blank=True)
    intro_last_exc = models.TextField(_('Descripcion de la experiencia'),blank=True)
    
    region = models.ForeignKey('Region')
       
    class Meta:
        ordering = ('date',)
        verbose_name = _('Excursion')
        verbose_name_plural = _('Listado de Excursiones')
        get_latest_by = 'date'
        
    def __unicode__(self):
        return self.name
        
    def thumb_photo_post_excurtion(self):
        thumbs = self.photopostexcurtion_set.all()
        if thumbs:  
            return thumbs[0].photo.url_280x80
        else:
            return self.foto_carrusel_uno.url_280x80
        
class PhotoPostExcurtion(models.Model):
    excurtion = models.ForeignKey(Excurtion)
    photo = ImageWithThumbsField(name=str(excurtion),blank=True,upload_to="./img/excurtion", sizes=((280,80)))

    class Meta:
        ordering = ('excurtion',)
        verbose_name = _('Foto Post Excursion')
        verbose_name_plural = _('Listado de Fotos Post Excursion')
        get_latest_by = 'excurtion'
        
    def __unicode__(self):
        return self.name
        
class NextExcurtionFeed(Feed):
    title = "Sendero Norte - Noticias"
    description = "Noticias de Sendero Norte Expediciones"
    link="/contact/send"
    
    def items(self):
        return Excurtion.objects.all().order_by('-next_date')[:5]
    
    def item_title(self, item):
        return item.name
    
    def item_link(self,item):
        return "http://senderonorte.com.ar/excurtion_detail/"+str(item.id)+"/excurtion"

    def item_description(self, item):
        return item.description
        

