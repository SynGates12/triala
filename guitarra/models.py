from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible 
class Forma (models.Model):
    forma = models.CharField(max_length=100)
    
    def __str__(self):
        return self.forma 
    
@python_2_unicode_compatible     
class N_cordes (models.Model):
    num = models.CharField(max_length=100)
    
    def __str__(self):
        return self.num 
    
@python_2_unicode_compatible     
class Fusta_c (models.Model):
    fusta_c = models.CharField(max_length=100)
    
    def __str__(self):
        return self.fusta_c 
    
@python_2_unicode_compatible     
class Fusta_d (models.Model):
    fusta_d = models.CharField(max_length=100)
    
    def __str__(self):
        return self.fusta_d 
    
@python_2_unicode_compatible     
class Pastilles (models.Model):
    pastilles = models.CharField(max_length=100)
    def __str__(self):
        return self.pastilles 
    
@python_2_unicode_compatible     
class Tremolo (models.Model):
    tremolo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tremolo 
    
@python_2_unicode_compatible     
class Color (models.Model):
    color = models.CharField(max_length=100)
    
    def __str__(self):
        return self.color

@python_2_unicode_compatible 
class Estil_musica (models.Model):
    nom_estil = models.CharField(max_length=150)
    descripcio_estil = models.TextField(max_length=3000)
    imatge = models.ImageField(upload_to='media',
                              blank=True)
    
    def __str__(self):
        return self.nom_estil                          
    
@python_2_unicode_compatible    
class Grup (models.Model):
    nom_grup = models.CharField(max_length=150)
    descripcio_grup = models.CharField(max_length=1000)
    pedals = models.CharField(max_length=1000, null = True)
    amplis = models.CharField(max_length=1000, null = True)
    imatge = models.ImageField(upload_to='media',
                              blank=True)
                            
    def __str__(self):
        return self.nom_grup
    
        
    
class Guitarra (models.Model):
    nom_guitarra = models.CharField(max_length=300, null=True,)
    descripcio_guitarra = models.TextField(max_length=3000, null=True,)
    preu = models.IntegerField(null=True,)
    color = models.ForeignKey(Color,on_delete=models.CASCADE,)
    forma = models.ForeignKey(Forma,on_delete=models.CASCADE,)
    n_cordes = models.ForeignKey(N_cordes,on_delete=models.CASCADE,)
    fusta_c = models.ForeignKey(Fusta_c,on_delete=models.CASCADE,)
    fusta_d = models.ForeignKey(Fusta_d,on_delete=models.CASCADE,)
    pastilles = models.ForeignKey(Pastilles,on_delete=models.CASCADE,)
    tremolo = models.ForeignKey(Tremolo,on_delete=models.CASCADE,)
    grup = models.ManyToManyField(Grup)
    estil = models.ManyToManyField(Estil_musica)
    imatge = models.ImageField(upload_to='media',
                              blank=True)
    logo = models.ImageField(upload_to='media',
                              blank=True)                          
                              
                           