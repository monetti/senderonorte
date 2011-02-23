from django.db import models
from django.utils.translation import ugettext_lazy as _

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from thumbs import ImageWithThumbsField
    
import datetime

class Excurtion(models.Model):
    name = models.CharField(_("Nombre"),max_length="200")
    description = models.TextField(_("Descripcion"))
    summary = models.TextField(_("Resumen"))
    next_date = models.DateTimeField(_("Proxima Fecha"))
    place = models.CharField(_('Lugar'),max_length="200")
    time = models.CharField(_('Horario'),max_length="200")
    duration = models.CharField(_("Duracion"),max_length="10")
    
    foto_carrusel_uno = ImageWithThumbsField(name="photo_carrusel_one",upload_to="./img/excurtion", sizes=((540,340),(280,80),))
    foto_carrusel_dos = ImageWithThumbsField(name="photo_carrusel_two",upload_to="./img/excurtion")
    foto_carrusel_tres = ImageWithThumbsField(name="photo_carrusel_three",upload_to="./img/excurtion")
           
    publish_last_exc = models.BooleanField(_("Publicar en Ultimas Excursiones?"), default=False,blank=True)
    intro_last_exc = models.TextField(_('Descripcion de la experiencia'),blank=True)
       
    class Meta:
        ordering = ('next_date',)
        verbose_name = _('Excursion')
        verbose_name_plural = _('Lista de Excursiones')
        get_latest_by = 'next_date'
        
    def __unicode__(self):
        return self.name
        
    def thumb_photo_post_excurtion(self):
        thumbs = self.photopostexcurtion_set.all()
        if thumbs:  
            return thumbs[0].photo.url_280x80
        else:
            return self.foto_carrusel_uno.url_530x330
        
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
