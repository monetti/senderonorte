from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
import datetime

class ActivitieRegion(models.Model):
    slug = models.SlugField(editable=False)
    name = models.CharField(_("Nombre"),max_length="200")
    description = models.TextField(_("Descripcion"),blank=True)

    def save(self):
        self.slug = slugify(self.name)
        super(ActivitieRegion, self).save()
        
    class Meta:
        verbose_name = _('Region de Actividad')
        verbose_name_plural = _('Regiones de Actividades')

    def __unicode__(self):
        return self.name
    
class Activitie(models.Model):
    name = models.CharField(_("Nombre"),max_length="200")
    description = models.TextField(_("Descripcion"))
    region = models.ForeignKey('ActivitieRegion')
    duration = models.IntegerField(_("Duracion"),max_length="10")
    photo = models.ImageField(_("Foto"),upload_to="img/activities")
    publish_newsletter = models.BooleanField(_("Publicar en NewsLetter"), default=False,blank=True) 

    class Meta:
        ordering = ('region',)
        verbose_name = _('Actividad')
        verbose_name_plural = _('Listado de Actividades')
        get_latest_by = 'region'
        
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return u'/activitie_detail/%s' % self.id

       

