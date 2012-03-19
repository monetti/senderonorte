from django.db import models

class Video(models.Model):
    link = models.URLField()
    
    def __str__(self):
        return self.link


        
