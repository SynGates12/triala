from django.conf.urls import url
from guitarra import views

app_name='guitarra'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^grups/$', views.grups, name="grups"),
    url(r'^estils/$', views.estils, name="estils")
]