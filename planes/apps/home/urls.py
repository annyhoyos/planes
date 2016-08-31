from django.conf.urls.defaults import patterns, url
from.views import BuscarView
from.models import *

urlpatterns = patterns('planes.apps.home.views',
	url(r'^$','index_view', name ='vista_principal'),
	url(r'^login/$','login_view', name= 'vista_login'),
	url(r'^logout/$','logout_view', name= 'vista_logout'),
	url(r'^plan/(?P<id_prod>.*)/$', 'single_planes_view', name = 'vista_single_planes'),
	url(r'^planes/page/(?P<pagina>.*)/$','planes_view', name='vista_planes'),
	url(r'^registro/$','register_view',name='vista_registro'),
	url(r'^buscar/$','buscar_view', name= 'vista_buscar'),
	url(r'^buscar/$','BuscarView', name ='vista_buscar'),
	
)