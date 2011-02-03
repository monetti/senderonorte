from django.db import models
from django.utils.translation import ugettext_lazy as _

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

import datetime

class Excurtion(models.Model):
    name = models.CharField(_("Nombre"),max_length="200")
    description = models.TextField(_("Descripcion"))
    summary = models.CharField(_("Resumen"),max_length="500")
    next_date = models.DateTimeField(_("Proxima Fecha"))
    place = models.CharField(_('Lugar'),max_length="200")
    time = models.CharField(_('Horario'),max_length="200")
    duration = models.CharField(_("Duracion"),max_length="10")
    photo = models.ImageField(_("Foto"),upload_to="media/")
    
    class Meta:
        ordering = ('next_date',)
        verbose_name = _('Excursion')
        verbose_name_plural = _('Listas de Excursiones')
        get_latest_by = 'next_date'
        
    def __unicode__(self):
        return self.name
