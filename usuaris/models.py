from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from guitarra.models import Guitarra

# Create your models here.
class Perfil (models.Model):
     usuari = models.OneToOneField(User)
     is_admin = models.BooleanField(default=False)
     
class Comentari (models.Model):
    data = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=1000)
    guitarra = models.ForeignKey('guitarra.Guitarra',on_delete=models.CASCADE)
    usuari=models.ForeignKey(Perfil,on_delete=models.SET_NULL,blank=True, null=True, related_name="comentari")

     

def post_save_user(sender, instance, created, **kwargs):
    if created:
        nou_perfil = Perfil.objects.create(
                    usuari=instance,
                    )
        instance.refresh_from_db()

post_save.connect(post_save_user, sender=User)     

