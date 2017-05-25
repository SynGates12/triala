from django.conf.urls import url
from guitarra import views

app_name='guitarra'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^grups/$', views.grups, name="grups"),
    url(r'^estils/$', views.estils, name="estils"),
    url(r'^formes/$', views.formes, name="formes"),
    url(r'^guitarres/$', views.guitarres, name="guitarres"),
    url(r'^afegir_guitarra/$', views.afegir_guitarra, name="afegir_guitarra"),
    url(r'^afegir_grup/$', views.afegir_grup, name="afegir_grup"),
    url(r'^afegir_estil/$', views.afegir_estil, name="afegir_estil"),
    url(r'^afegir_guitarra/$', views.afegir_guitarra, name="afegir_guitarra"),
    url(r'^estil_informacio/(?P<estil_id>\d+)$', views.estil_informacio, name="estil_informacio"),
    url(r'^grup_informacio/(?P<grup_id>\d+)$', views.grup_informacio, name="grup_informacio"),
    url(r'^guitarra_informacio/(?P<guitarra_id>\d+)$', views.guitarra_informacio, name="guitarra_informacio"),
    url(r'^(?P<forma_id>\d+)/$', views.n_cordes, name="n_cordes"),
    url(r'^(?P<forma_id>\d+)/(?P<n_cordes_id>\d+)$', views.fusta_c, name="fusta_c"),
    url(r'^(?P<forma_id>\d+)/(?P<n_cordes_id>\d+)/(?P<fusta_c_id>\d+)$', views.fusta_d, name="fusta_d"),
    url(r'^(?P<forma_id>\d+)/(?P<n_cordes_id>\d+)/(?P<fusta_c_id>\d+)/(?P<fusta_d_id>\d+)$', views.pastilles, name="pastilles"),
    url(r'^(?P<forma_id>\d+)/(?P<n_cordes_id>\d+)/(?P<fusta_c_id>\d+)/(?P<fusta_d_id>\d+)/(?P<pastilles_id>\d+)$', views.tremolo, name="tremolo"),
    url(r'^(?P<forma_id>\d+)/(?P<n_cordes_id>\d+)/(?P<fusta_c_id>\d+)/(?P<fusta_d_id>\d+)/(?P<pastilles_id>\d+)/(?P<tremolo_id>\d+)$', views.imatge_final, name="imatge_final")
    

]