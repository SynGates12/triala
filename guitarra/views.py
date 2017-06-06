# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from guitarra.models import Forma, N_cordes, Fusta_c, Fusta_d, Pastilles, Tremolo, Grup, Estil_musica, Guitarra
from guitarra.forms import nou_grup, nou_estil, ComentaForm
from usuaris.models import Perfil, Comentari
from django.forms import modelform_factory
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "guitarra/index.html")
    
def grups(request):
    tots_grups = Grup.objects.all()
    ctx = {'llista_grups' : tots_grups}
    return render (request, "guitarra/grups.html", ctx)

def grup_informacio(request, grup_id):
    grup = get_object_or_404(Grup,pk=grup_id)
    guitarra_grup = grup.guitarra_set.all()
    return render(request,"guitarra/grup_informacio.html",{'grup': grup, 'guitarra_grup':guitarra_grup})

def estils(request):
    tots_estils = Estil_musica.objects.all()
    ctx = {'llista_estils' : tots_estils}
    return render (request, "guitarra/estils.html", ctx)
    
def estil_informacio(request, estil_id):
    estil = get_object_or_404(Estil_musica,pk=estil_id)
    guitarra_estil = estil.guitarra_set.all()
    return render(request,"guitarra/estil_informacio.html", {'estil': estil, 'guitarra_estil':guitarra_estil})    
    
def guitarres(request):
    totes_guitarres = Guitarra.objects.all()
    ctx = {'llista_guitarres' : totes_guitarres}
    return render (request, "guitarra/guitarres.html", ctx)    
    
def guitarra_informacio(request, guitarra_id):
    guitarra = get_object_or_404(Guitarra,pk=guitarra_id)
    
    if request.user:
        usuari=request.user
    
        if request.method == 'POST':
            form = ComentaForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['text']
                Comentari.objects.create (text = text, guitarra= guitarra, usuari = usuari.perfil)
                messages.info(request, "Comentari afegit correctament")
                return redirect(request.META['HTTP_REFERER'])
        else:
             form = ComentaForm()
        
        for f in form.fields:
           form.fields[f].widget.attrs['class'] = 'form-control'
           form.fields['text'].widget.attrs['rows'] = '4'
           form.fields['text'].widget.attrs['placeholder']="Comenta..."
    
        comentari = guitarra.comentari_set.all()
    # ctx={'guitarra': guitarra}
    # return render(request,"guitarra/guitarra_informacio.html",ctx) s
        return render (request, 'guitarra/guitarra_informacio.html', {'guitarra':guitarra,'form': form, 'comentari':comentari } )
    
    else:
        return redirect ('login')    
    
def formes(request):
    totes_formes = Forma.objects.all();
    ctx={'llista_formes' : totes_formes};
    return render (request, "guitarra/formes.html", ctx)
    
def n_cordes(request, forma_id):
    formes = get_object_or_404(Forma,pk=forma_id)
    forma_cordes =  N_cordes.objects.filter( guitarra__forma = formes  ).distinct() 
    return render (request, "guitarra/n_cordes.html", {'formes':formes, 'forma_cordes':forma_cordes})
    
def fusta_c(request, forma_id, n_cordes_id):
    forma = get_object_or_404(Forma,pk=forma_id)
    fustac = get_object_or_404(N_cordes,pk=n_cordes_id)
    cordes_fustac =  Fusta_c.objects.filter( guitarra__n_cordes = fustac  ).distinct() 
    return render (request, "guitarra/fusta_c.html", {'fustac':fustac, 'cordes_fustac':cordes_fustac, 'forma':forma})
    
def fusta_d(request, forma_id, n_cordes_id, fusta_c_id):
    forma = get_object_or_404(Forma,pk=forma_id)
    n_cordes = get_object_or_404(N_cordes,pk=n_cordes_id)
    fusta_c_d =  get_object_or_404(Fusta_c,pk=fusta_c_id)
    llista_fusta =  Fusta_d.objects.filter( guitarra__fusta_c = fusta_c_d  ).distinct() 
    return render (request, "guitarra/fusta_d.html", {'forma':forma, 'n_cordes':n_cordes, 'fusta_c_d': fusta_c_d, 'llista_fusta':llista_fusta})
    
def pastilles(request, forma_id, n_cordes_id, fusta_c_id, fusta_d_id):
    forma = get_object_or_404(Forma,pk=forma_id)
    n_cordes = get_object_or_404(N_cordes,pk=n_cordes_id)
    fusta_c =  get_object_or_404(Fusta_c,pk=fusta_c_id)
    fustad_pastilles = get_object_or_404(Fusta_d,pk=fusta_d_id)
    list_pastilles = Pastilles.objects.filter(guitarra__fusta_d = fustad_pastilles ).distinct()
    return render (request, "guitarra/pastilles.html", {'fustad_pastilles':fustad_pastilles, 
                                                        'list_pastilles':list_pastilles,
                                                        'forma':forma,
                                                        'n_cordes':n_cordes,
                                                        'fusta_c':fusta_c,
                                                        })    

def tremolo(request, forma_id, n_cordes_id, fusta_c_id, fusta_d_id, pastilles_id):
    forma = get_object_or_404(Forma,pk=forma_id)
    n_cordes = get_object_or_404(N_cordes,pk=n_cordes_id)
    fusta_c =  get_object_or_404(Fusta_c,pk=fusta_c_id)
    fusta_d =  get_object_or_404(Fusta_d,pk=fusta_d_id)
    pastilles_tremolo = get_object_or_404(Pastilles,pk=pastilles_id)
    list_tremolo = Tremolo.objects.filter(guitarra__pastilles = pastilles_tremolo).distinct()
    return render (request, "guitarra/tremolo.html", {  'forma':forma,
                                                        'n_cordes':n_cordes,
                                                        'fusta_c':fusta_c,
                                                        'fusta_d':fusta_d,
                                                        'pastilles_tremolo':pastilles_tremolo,
                                                        'list_tremolo':list_tremolo
                                                        })



def imatge_final(request, forma_id, n_cordes_id, fusta_c_id, fusta_d_id, pastilles_id, tremolo_id):
     forma = get_object_or_404(Forma,pk=forma_id)
     n_cordes = get_object_or_404(N_cordes,pk=n_cordes_id)
     fusta_c =  get_object_or_404(Fusta_c,pk=fusta_c_id)
     fusta_d =  get_object_or_404(Fusta_d,pk=fusta_d_id)
     pastilles_tremolo = get_object_or_404(Pastilles,pk=pastilles_id)
     guit = get_object_or_404(Tremolo,pk=tremolo_id)
     list_guitarres = guit.guitarra_set.all()
     juano=get_object_or_404(Tremolo,pk=tremolo_id)
     guitarra=Guitarra.objects.filter(forma=forma,
                                      n_cordes=n_cordes,
                                      fusta_c=fusta_c,
                                      fusta_d=fusta_d,
                                      pastilles=pastilles_tremolo,
                                      tremolo=juano
                                           )
     list_guitarres=guitarra.values_list()
     return render (request, "guitarra/imatge_final.html", {'juano':juano,'list_guitarres':list_guitarres, 'guitarra':guitarra})  






def afegir_grup(request):
    if request.method == 'POST':
        form = nou_grup(request.POST, request.FILES)
        if form.is_valid():
            nom_grup = form.cleaned_data['nom_grup']
            repetit = Grup.objects.filter( nom_grup = nom_grup )
        
            if repetit:
                messages.error( request, "Aquest grup ja existeix")
            else:
                descripcio_grup = form.cleaned_data['descripcio_grup']
                pedals = form.cleaned_data['pedals']
                amplis = form.cleaned_data['amplis']
                imatge = form.cleaned_data['imatge']
                
                Grup.objects.create (nom_grup = nom_grup, descripcio_grup = descripcio_grup, pedals = pedals, amplis = amplis, imatge = imatge)
                
                messages.info(request, "Grup afegit correctament")
                return redirect ("guitarra:grups")
    else:
        form = nou_grup()
        
    for f in form.fields:
       form.fields[f].widget.attrs['class'] = 'form-group formularis'
       
    form.fields['nom_grup'].widget.attrs['placeholder']="Nom del Grup"
    form.fields['descripcio_grup'].widget.attrs['placeholder']="Descripció del grup"
    form.fields['pedals'].widget.attrs['placeholder']="Pedals del grup"
    form.fields['amplis'].widget.attrs['placeholder']="Amplificadors del grup"
    form.fields['nom_grup'].widget.attrs['required']="required"
    form.fields['descripcio_grup'].widget.attrs['required']="required"    
            
    return render (request, 'guitarra/afegir_grup.html', {'form': form} )        


        
def afegir_estil(request):
    if request.method == 'POST':
        form_estil = nou_estil(request.POST, request.FILES)
        if form_estil.is_valid():
            nom_estil = form_estil.cleaned_data['nom_estil']
            repetit = Estil_musica.objects.filter( nom_estil = nom_estil )
        
            if repetit:
                messages.error( request, "Aquest estil ja existeix")
            else:
                descripcio_estil = form_estil.cleaned_data['descripcio_estil']
                imatge = form_estil.cleaned_data['imatge']
                
                Estil_musica.objects.create (nom_estil = nom_estil, descripcio_estil = descripcio_estil, imatge = imatge)
                
                messages.info(request, "Estil afegit correctament")
                return redirect ("guitarra:estils")
    else:
        form_estil = nou_estil()
        
    for f in form_estil.fields:
       form_estil.fields[f].widget.attrs['class'] = 'form-group formularis'
       
    form_estil.fields['nom_estil'].widget.attrs['placeholder']="Nom del Estil"
    form_estil.fields['descripcio_estil'].widget.attrs['placeholder']="Descripció del estil"
    form_estil.fields['nom_estil'].widget.attrs['required']="required"
    form_estil.fields['descripcio_estil'].widget.attrs['required']="required"    
            
    return render (request, 'guitarra/afegir_estil.html', {'form_estil': form_estil} )
    
    
    
def afegir_guitarra(request):
    formulario_g = modelform_factory(model=Guitarra, exclude=[''])
    
    if request.method == 'POST':
        form_guitarra = formulario_g(request.POST, request.FILES)
        if form_guitarra.is_valid():
            form_guitarra.save()
            messages.info(request, "Guitarra afegida correctament")
            return redirect ("guitarra:guitarres")
            
    else:
        form_guitarra = formulario_g()
        
    for f in form_guitarra.fields:
       form_guitarra.fields[f].widget.attrs['class'] = 'form-group formularis'
       
    form_guitarra.fields['nom_guitarra'].widget.attrs['placeholder']="Model de la guitarra"
    form_guitarra.fields['descripcio_guitarra'].widget.attrs['placeholder']="Descripció de la guitarra"
    form_guitarra.fields['nom_guitarra'].widget.attrs['required']="required"
    form_guitarra.fields['descripcio_guitarra'].widget.attrs['required']="required"
    form_guitarra.fields['forma'].widget.attrs['required']="required"
    form_guitarra.fields['n_cordes'].widget.attrs['required']="required"
    form_guitarra.fields['fusta_c'].widget.attrs['required']="required"
    form_guitarra.fields['fusta_d'].widget.attrs['required']="required"
    form_guitarra.fields['pastilles'].widget.attrs['required']="required"
    form_guitarra.fields['tremolo'].widget.attrs['required']="required"
    form_guitarra.fields['imatge'].widget.attrs['required']="required"
    form_guitarra.fields['descripcio_guitarra'].widget.attrs['textarea']="textarea"
    
    
    return render (request, 'guitarra/afegir_guitarra.html', {'form_guitarra': form_guitarra} )
   
    
#EDITAR GUITARRA EXISTENT
def editar_guitarra(request, guitarra_id):
    EditForm = modelform_factory(Guitarra, fields=('nom_guitarra', 
                                                   'descripcio_guitarra',
                                                   'preu',
                                                   'color',
                                                   'forma',
                                                   'n_cordes',
                                                   'fusta_c',
                                                   'fusta_d',
                                                   'pastilles',
                                                   'tremolo',
                                                   'grup',
                                                   'estil',
                                                   'imatge',
                                                   'logo'))
    unEdit = Guitarra()
    
    #comprovem que existeix la guitarra
    if guitarra_id:
        unEdit = get_object_or_404(Guitarra, pk=guitarra_id)
        
    if request.method == 'POST':
        form = EditForm (request.POST,request.FILES, instance= unEdit)
        if form.is_valid():
           form.save()
           messages.info(request,"guitarra canviada correctament")
           return redirect("guitarra:guitarres")    
    else:
        form= EditForm (instance = unEdit)
    
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-group formularis'
 
    form.fields['nom_guitarra'].widget.attrs['placeholder']="Model de la guitarra"
    form.fields['descripcio_guitarra'].widget.attrs['placeholder']="Descripció de la guitarra"
    
    return render (request, 'guitarra/editar_guitarra.html', {'form': form} )    

#ESBORRAR DISC -----
def eliminar_guitarra(request, guitarra_id):
    guitarra = Guitarra.objects.get(id=guitarra_id)
    
    #si el métode és POST
    if request.method == 'POST':
        guitarra.delete()
        return redirect('guitarra:guitarres')

    else:
        return render(request, 'guitarra/eliminar_guitarra.html', {'guitarra': guitarra})
        
        

#EDITAR GRUP EXISTENT
def editar_grup(request, grup_id):
    EditForm = modelform_factory(Grup, fields=('nom_grup', 'descripcio_grup', 'pedals', 'amplis', 'imatge' ))
    unEdit = Grup()
    
    #comprovem que existeix el grup
    if grup_id:
        unEdit = get_object_or_404(Grup, pk=grup_id)
        
    if request.method == 'POST':
        form = EditForm (request.POST,request.FILES, instance= unEdit)
        if form.is_valid():
           form.save()
           messages.info(request,"grup canviat correctament")
           return redirect("guitarra:grups")    
    else:
        form= EditForm (instance = unEdit)
    
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-group formularis'
 
    form.fields['nom_grup'].widget.attrs['placeholder']="Nom del grup"
    form.fields['descripcio_grup'].widget.attrs['placeholder']="Descripció del grup"
    form.fields['pedals'].widget.attrs['placeholder']="Pedals del grup"
    form.fields['amplis'].widget.attrs['placeholder']="Amplificadors del grup"
    
    
    return render (request, 'guitarra/editar_grup.html', {'form': form} )    

#ESBORRAR GRUP -----
def eliminar_grup(request, grup_id):
    grup = Grup.objects.get(id=grup_id)
    
    #si el métode és POST
    if request.method == 'POST':
        grup.delete()
        return redirect('guitarra:grups')

    else:
        return render(request, 'guitarra/eliminar_grup.html', {'grup': grup})        



#EDITAR ESTIL EXISTENT
def editar_estil(request, estil_musica_id):
    EditForm = modelform_factory(Estil_musica, fields=('nom_estil', 'descripcio_estil', 'imatge' ))
    unEdit = Estil_musica()
    
    #comprovem que existeix l'estil
    if estil_musica_id:
        unEdit = get_object_or_404(Estil_musica, pk=estil_musica_id)
        
    if request.method == 'POST':
        form = EditForm (request.POST,request.FILES, instance= unEdit)
        if form.is_valid():
           form.save()
           messages.info(request,"estil canviat correctament")
           return redirect("guitarra:estils")    
    else:
        form= EditForm (instance = unEdit)
    
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-group formularis'
 
    form.fields['nom_estil'].widget.attrs['placeholder']="Nom de l'estil"
    form.fields['descripcio_estil'].widget.attrs['placeholder']="Descripció de l'estil"
    
    
    return render (request, 'guitarra/editar_estil.html', {'form': form} )    

#ESBORRAR DISC -----
def eliminar_estil(request, estil_musica_id):
    estil = Estil_musica.objects.get(id=estil_musica_id)
    
    #si el métode és POST
    if request.method == 'POST':
        estil.delete()
        return redirect('guitarra:estils')

    else:
        return render(request, 'guitarra/eliminar_estil.html', {'estil': estil})