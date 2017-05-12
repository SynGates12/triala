from django.conf.urls import url
from guitarra import views

app_name='guitarra'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^grups/$', views.grups, name="grups"),
    url(r'^estils/$', views.estils, name="estils"),
    url(r'^formes/$', views.formes, name="formes"),
    url(r'^afegir_guitarra/$', views.afegir_guitarra, name="afegir_guitarra"),
    url(r'^afegir_grup/$', views.afegir_grup, name="afegir_grup")

]