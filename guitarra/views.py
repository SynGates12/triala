from django.shortcuts import render,get_object_or_404,redirect, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from guitarra.models import Forma, N_cordes, Fusta_c, Fusta_d, Pastilles, Tremolo, Grup, Estil_musica, Guitarra
from usuaris.models import Perfil, Comentari
from django.forms import modelform_factory
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, "guitarra/index.html")
    
def grups(request):
    tots_grups = Grup.objects.all();
    ctx = {'llista_grups' : tots_grups}
    return render (request, "guitarra/grups.html", ctx)
    
def estils(request):
    tots_estils = Estil_musica.objects.all();
    ctx = {'llista_estils' : tots_estils}
    return render (request, "guitarra/estil.html", ctx)