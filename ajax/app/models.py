from distutils.command.upload import upload
from django.db import models

class Personne(models.Model):
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    nom = models.CharField(max_length=100)
    numero = models.IntegerField()
    date_save = models.DateTimeField()
    
    class Meta:
        verbose_name=('Personne')
        verbose_name_plural=('Personnes')
        
    def __str__(self):
        return self.nom
    
