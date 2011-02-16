from django.db import models
from django.utils.translation import ugettext_lazy as _

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

import datetime

class Excurtion(models.Model):
    name = models.CharField(_("Nombre"),max_length="200")
    description = models.TextField(_("Descripcion"))
    summary = models.TextField(_("Resumen"))
    next_date = models.DateTimeField(_("Proxima Fecha"))
    place = models.CharField(_('Lugar'),max_length="200")
    time = models.CharField(_('Horario'),max_length="200")
    duration = models.CharField(_("Duracion"),max_length="10")
    photo = models.ImageField(_("Foto"),upload_to="./img/excurtion")

    photo_2 = models.ImageField(_("Foto Post Excursion I"),blank=True,upload_to="./img/excurtion")
    photo_3 = models.ImageField(_("Foto Post Excursion II"),blank=True,upload_to="./img/excurtion")
    photo_4 = models.ImageField(_("Foto Post Excursion III"),blank=True,upload_to="./img/excurtion")
    photo_5 = models.ImageField(_("Foto Post Excursion IV"),blank=True,upload_to="./img/excurtion")
    photo_6 = models.ImageField(_("Foto Post Excursion V"),blank=True,upload_to="./img/excurtion")
        
    published_last_exc = models.BooleanField(_("Publicar en Ultimas Excursiones"), default=False)
    intro_last_exc = models.CharField(_('Texto Resumen Ultima Excursion'),blank=True,max_length="100")
       
    class Meta:
        ordering = ('next_date',)
        verbose_name = _('Excursion')
        verbose_name_plural = _('Lista de Excursiones')
        get_latest_by = 'next_date'
        
    def __unicode__(self):
        return self.name
