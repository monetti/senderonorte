from django.db import models
from django.utils.translation import ugettext_lazy as _

import datetime


# Create your models here.
class New(models.Model):
    title = models.CharField(_("Titulo"),max_length="200")
    summary = models.CharField(_("Resumen"),max_length="200")
    description = models.CharField(_("Descripcion"),max_length="200")
    create_date = models.DateTimeField(_("Fecha de Creacion"),)
    create_date.input_formats=['%d-%m-%Y']
    image = models.ImageField(_("Foto"),upload_to="media/")
    
    class Meta:
        ordering = ('create_date',)
        verbose_name = _('Novedad')
        verbose_name_plural = _('Lista de Novedades')
        get_latest_by = 'create_date'
        
    def __unicode__(self):
        return self.title
