from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Cimbling(models.Model):
    cimbling_type = models.CharField(_("Tipo de Excursion"),max_length="200")
    summary = models.TextField(_("Resumen"))
       
    photo = models.ImageField(_("Foto"),upload_to="./img/cimblings")
               
    class Meta:
        ordering = ('cimbling_type',)
        verbose_name = _('Escalada')
        verbose_name_plural = _('Listado de Escaladas')
        
    def __unicode__(self):
        return self.cimbling_type

