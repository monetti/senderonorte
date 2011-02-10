from django.db import models
from django.utils.translation import ugettext_lazy as _

import datetime


# Create your models here.
class New(models.Model):
    title = models.CharField(_("Titulo"),max_length="200")
    summary = models.TextField(_("Resumen"))
    description = models.TextField(_("Descripcion"))
    created_date = models.DateTimeField(_("Fecha de Creacion"),)
    image = models.ImageField(_("Foto"),upload_to="media/")
    
    class Meta:
        ordering = ('created_date',)
        verbose_name = _('Novedad')
        verbose_name_plural = _('Lista de Novedades')
        get_latest_by = 'created_date'
        
    def __unicode__(self):
        return self.title
