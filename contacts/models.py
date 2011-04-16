from django.db import models
from django.utils.translation import ugettext_lazy as _

class Contact(models.Model):
    name = models.CharField(_("Nombre"), max_length=50, blank=True)
    last_name = models.CharField(_("Apellido"), max_length=50, blank=True)
    email = models.CharField(_("E-mail"), max_length=50)    

    class Meta:
        ordering = ('email',)
        verbose_name = _('Contacto')
        verbose_name_plural = _('Lista de Contactos')
        get_latest_by = 'email'
        
    def __unicode__(self):
        return self.email

    
    
    
    
