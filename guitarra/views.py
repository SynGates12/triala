# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from guitarra.models import Forma, N_cordes, Fusta_c, Fusta_d, Pastilles, Tremolo, Grup, Estil_musica, Guitarra
from guitarra.forms import nou_grup
from usuaris.models import Perfil, Comentari
from django.forms import modelform_factory
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "guitarra/index.html")
    
def grups(request):
    tots_grups = Grup.objects.all();
    ctx = {'llista_grups' : tots_grups};
    return render (request, "guitarra/grups.html", ctx);
    
def estils(request):
    tots_estils = Estil_musica.objects.all();
    ctx = {'llista_estils' : tots_estils};
    return render (request, "guitarra/estil.html", ctx);
    
def formes(request):
    totes_formes = Forma.objects.all();
    ctx={'llista_formes' : totes_formes};
    return render (request, "guitarra/formes.html", ctx)

def afegir_grup(request):
    if request.method == 'POST':
        form = nou_grup(request.POST, request.FILES)
        if form.is_valid():
            nom_grup = form.cleaned_data['nom grup']
            repetit = nom_grup.objects.filter( nom_grup = nom_grup )
        
            if repetit:
                messages.error( request, "Aquest grup ja existeix")
            else:
                descripcio_grup = form.cleaned_data['descripcio grup']
                image = form.cleaned_data['image']
                
                messages.info(request, "Grup afegit correctament")
                return redirect ("guitarra:grups")
    else:
        form = nou_grup()
        
    for f in form.fields:
       form.fields[f].widget.attrs['class'] = 'form-group formularis'
       
    form.fields['nom_grup'].widget.attrs['placeholder']="Nom del Grup"
    form.fields['descripcio_grup'].widget.attrs['placeholder']="Descripció del grup"
    form.fields['nom_grup'].widget.attrs['required']="required"
    form.fields['descripcio_grup'].widget.attrs['required']="required"    
            
    return render (request, 'guitarra/afegir_grup.html', {'form': form} )        
        
        
        
def afegir_guitarra(request):
    form_class = modelform_factory(Grup, exclude=[])
    if request.method == 'POST':
        form = form_class(request.POST, instance = Grup())
        if form.is_valid():
            form.save()
            return redirect ('afegir_guitarra')
        
        else:
            form = form_class(instance = Grup() )
        for f in form.fields:
            form.fields[f].widget.attrs['class'] = 'form-control'
        
        return render (request, 'afegir_guitarra', {'form':form,})
        