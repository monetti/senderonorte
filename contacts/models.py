from django.db import models
from django.utils.translation import ugettext_lazy as _

class ContactGroup(models.Model):
    name = models.CharField(_("Nombre"),max_length=50)
    description = models.TextField(_("Descripcion"),blank=True)        
    
    class Meta:
        ordering = ('name',)
        verbose_name = _('Grupo de Contacto')
        verbose_name_plural = _('Lista de Grupos de Contactos')
        get_latest_by = 'name'
        
    def __unicode__(self):
        return self.name

class Contact(models.Model):
    email = models.CharField(_("E-mail"), max_length=50)    
    grupo = models.ForeignKey(ContactGroup)
    name = models.CharField(_("Nombre"), max_length=50, blank=True)
    last_name = models.CharField(_("Apellido"), max_length=50, blank=True)
    

    class Meta:
        ordering = ('email',)
        verbose_name = _('Contacto')
        verbose_name_plural = _('Lista de Contactos')
        get_latest_by = 'email'
        
    def __unicode__(self):
        return self.email

    
    
    
    
