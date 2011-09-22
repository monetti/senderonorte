from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
    photo = models.ImageField(_("Foto"),upload_to="users",blank=True)
    user = models.ForeignKey(User, unique=True)
    description = models.TextField(_("Descripcion"),blank=True)
    
    def __unicode__(self):
        return self.user.last_name +', '+ self.user.first_name

    class Meta:
        verbose_name = _('Perfil de Usuario')
        verbose_name_plural = _('Listado de Perfiles Usuarios del Sitio')
        
class Logo(models.Model):
    photo = models.ImageField(_("Imagen"),upload_to="logos")
    url = models.CharField(_("URL"),max_length=100)
    
    class Meta:
        verbose_name = _('Logos')
        verbose_name_plural = _('Listado Logos')
