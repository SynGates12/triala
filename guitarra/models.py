from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Forma (models.Model):
    forma = models.CharField(max_length=100)
    
class N_cordes (models.Model):
    num = models.IntegerField()
    
class Fusta_c (models.Model):
    fusta_c = models.CharField(max_length=100)
    
class Fusta_d (models.Model):
    fusta_d = models.CharField(max_length=100)
    
class Pastilles (models.Model):
    pastilles = models.CharField(max_length=100)
    
class Tremolo (models.Model):
    tremolo = models.BooleanField()
    
class Grup (models.Model):
    nom_grup = models.CharField(max_length=150)
    descripcio_grup = models.CharField(max_length=500)
    
class Estil_musica (models.Model):
    nom_estil = models.CharField(max_length=150)
    descripcio_estil = models.CharField(max_length=500)
    
class Guitarra (models.Model):
    forma = models.ForeignKey(Forma, on_delete=models.CASCADE)
    n_cordes = models.ForeignKey(N_cordes, on_delete=models.CASCADE)
    fusta_c = models.ForeignKey(Fusta_c, on_delete=models.CASCADE)
    fusta_d = models.ForeignKey(Fusta_d, on_delete=models.CASCADE)
    pastilles = models.ForeignKey(Pastilles, on_delete=models.CASCADE)
    tremolo = models.ForeignKey(Tremolo, on_delete=models.CASCADE)
    grup = models.ForeignKey(Grup, on_delete=models.CASCADE)
    estil = models.ForeignKey(Estil_musica, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media',
                              blank=True)