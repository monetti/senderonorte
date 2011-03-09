from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class CustomizedTravel(models.Model):
    name = models.CharField(_("Nombre"),max_length="200")
    summary = models.TextField(_("Resumen"))
    duration = models.CharField(_("Duracion"),max_length="10")
    
    photo = models.ImageField(_("Foto"),upload_to="./img/customizedtravels")
               
    class Meta:
        ordering = ('name',)
        verbose_name = _('Viaje a Medida')
        verbose_name_plural = _('Listado de Viajes a Medida')
        
    def __unicode__(self):
        return self.name

