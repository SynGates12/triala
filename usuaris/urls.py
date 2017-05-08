from django.conf.urls import url
from usuaris import views

app_name='usuaris'

urlpatterns = [
    url(r'^crear/', views.crear_usuari,name="crear_usuari"),
    url(r'^modificar/', views.modificar_perfil,name="modificar_perfil"),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout')
   
]
