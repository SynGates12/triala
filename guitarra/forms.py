# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelChoiceField, ModelMultipleChoiceField
from .models import Grup, Estil_musica

    

#afegir Grup

class nou_grup (forms.Form):
    nom_grup = forms.CharField(max_length=120)
    descripcio_grup = forms.CharField(max_length=1000, widget=forms.Textarea)
    pedals = forms.CharField(max_length=1000, widget=forms.Textarea)
    amplis = forms.CharField(max_length=1000, widget=forms.Textarea)
    imatge = forms.ImageField(label='Selecciona un arxiu')
    
#afegir Estil    

class nou_estil (forms.Form):
    nom_estil = forms.CharField(max_length=120)
    descripcio_estil = forms.CharField(max_length=3000, widget=forms.Textarea)
    imatge = forms.ImageField(label='Selecciona un arxiu')
    
class ComentaForm(forms.Form):
    text=forms.CharField(label="Comenta...",widget=forms.Textarea)