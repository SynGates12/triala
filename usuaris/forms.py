from django import forms
from django.conf import settings
from .models import Perfil, Comentari
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):
    username=forms.CharField(label="Nom usuari",
                             max_length=200,
                             help_text="Nom d'usuari")
    password=forms.CharField(label="Paraula de pas",
                             max_length=24,
                             help_text="Contrasenya per entrar",
                             widget=forms.PasswordInput(),
                            )
                            
class nou_usuari_form(forms.Form):
    email=forms.EmailField(label="Correu",
                             max_length=200,
                             help_text="Correu")
    password=forms.CharField(label="Paraula de pas",
                             max_length=24,
                             help_text="Contrasenya per entrar",
                             widget=forms.PasswordInput(),
                            )
                            
# class Comenta(forms.Form):
#     text=forms.CharField(label="Comenta...",
#                         max_length=1000)
    

class GrupForm(forms.Form):
    name=forms.CharField(label="Nom Grup",
                         max_length=300)
    descripcio=forms.CharField(label="Descripcio grup",
                                max_length=1000)
                                
    