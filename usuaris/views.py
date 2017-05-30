# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import LoginForm, nou_usuari_form
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from usuaris.models import Perfil, Comentari
from guitarra.models import Forma, N_cordes, Fusta_c, Fusta_d, Pastilles, Tremolo, Grup, Estil_musica, Guitarra
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import ( login as authLogin,
                                  authenticate,
                                  logout as authLogout )
from django.contrib import messages

# Create your views here.
#CREAR USUARI -------
def crear_usuari(request, perfil_id=None):
    
    if request.method == 'POST':
        form = nou_usuari_form(request.POST )
        
        if form.is_valid():
            email = form.cleaned_data['email']
            repetit = User.objects.filter( username = email )
            #mirem si esta repetit i llencem missatge error 
            if repetit:
                messages.error( request, "Aquest nom d'usuari ja existeix")
            else:
                password = form.cleaned_data['password']
                #creem el nou usuari
                nou_usuari = User.objects.create_user( username = email, email = email, password = password )
                
                messages.info(request,"Usuari creat correctament")
                return redirect('guitarra:index')
    else:
        form = nou_usuari_form()
    
    for f in form.fields:
       form.fields[f].widget.attrs['class'] = 'inputForm'
       
    form.fields['email'].widget.attrs['placeholder']="Email"
    form.fields['password'].widget.attrs['placeholder']="Contrasenya"
    form.fields['email'].widget.attrs['required']="required"
    form.fields['password'].widget.attrs['required']="required"
    
    return render(request, 'crear_usuari.html', {'form': form,} )
    
    
#LOGEJAR-SE ------
def login(request):

    #si tot es POST:
    if request.method=='POST':
        form=LoginForm( request.POST )

        if form.is_valid():
            user=authenticate( username = form.cleaned_data['username'],
                               password = form.cleaned_data['password'])
               
            if user and user.is_active:
                #si tot és ok:
                authLogin( request, user )
                next = request.GET.get('next')
                messages.info(request,"Benvingut")
                return redirect(next or 'guitarra:index')

            else:
                messages.error(request,"Usuari o password incorrecte o usuari no actiu")
                print "error"
           
    else:
        form=LoginForm()
   
    ctx={ 'form':form, }
    form.fields['username'].widget.attrs['placeholder']="Email"
    form.fields['password'].widget.attrs['placeholder']="Contrasenya"
    form.fields['username'].widget.attrs['required']="required"
    form.fields['password'].widget.attrs['required']="required"
    
    return render(request, 'login.html', ctx )

#DESLOGUEJAR-SE: me voy! ---    
def logout(request):
    authLogout( request )
    return redirect( 'guitarra:index')
    
def modificar_perfil(request):
    usuariForm = modelform_factory(User,fields=("first_name","last_name"))
    unPerfil = request.user.perfil
    unUsuari = request.user
    
    if request.method == 'POST':
        formUsuari = usuariForm(request.POST, instance = unUsuari)
       
        formUsuariValid = formUsuari.is_valid()
        
            
        if formUsuariValid:
            formUsuari.save()
           
            messages.info(request,"S'han modificat les dades correctament")
            return redirect('guitarra:index')
    else:
        formUsuari = usuariForm(instance = unUsuari)
        
        
    for f in formUsuari.fields:
       formUsuari.fields[f].widget.attrs['class'] = 'formulari'
    
   
    formUsuari.fields['first_name'].widget.attrs['placeholder']="Nom"
    formUsuari.fields['last_name'].widget.attrs['placeholder']="Cognoms"
    
    return render(request, 'modificar_perfil.html', {'formUsuari': formUsuari } )    
                                                     
                                                     
def comenta(request):
    formulario_c = modelform_factory(model=Comentari, exclude=[''])
   
    if request.method == 'POST':
        form_comenta = formulario_c(request.POST)
        
        if form_comenta.is_valid():
            form_comenta.save()
            messages.info(request, "Comentari afegit correctament")
            return redirect ("guitarra:guitarra_informacio")
            
    else:
        form_comenta = formulario_c()
        
    for f in form_comenta.fields:
       form_comenta.fields[f].widget.attrs['class'] = 'form-group formularis'
       
    return render (request, 'guitarra/guitarra_informacio.html', {'form_comenta': form_comenta} )
    
    
    
#     usuari = Perfil.objects.get(id=perfil_id)
    
#     if request.method == 'POST':
#         form_comenta = Comenta(request.POST)
        
#         if form_comenta.is_valid():
#             text = form_comenta.cleaned_data['text']
        
#             form_comenta.save()
#             Comentari.objects.create(text=text,
#                                      usuari=usuari
#                                     )
                                    
#             return redirect("guitarra:guitarra_informacio")    
#     else:
#         form_comenta= Comenta()
    
#     for f in form_comenta.fields:
#         form_comenta.fields[f].widget.attrs['class'] = 'form-group formularis'
        
#     return render (request, 'guitarra/guitarra_informacio.html', {'form_comenta': form_comenta} )

def llista_comentaris(request, guitarra_id):
    guitarra = get_object_or_404(Guitarra,pk=guitarra_id)
    comentari = guitarra.comentari_set.all()
    return render(request,"guitarra/guitarra_informacio.html", {'guitarra': guitarra, 'comentari':comentari}) 
    
    
    
    