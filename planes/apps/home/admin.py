from django.contrib import admin
from planes.apps.home.models import Planes, Hotel, Destino, Transporte, Descripcion, Servicios
from planes.apps.home.models import user_profile


admin.site.register(Planes)
admin.site.register(Hotel)
admin.site.register(Destino)
admin.site.register(Transporte)
admin.site.register(Descripcion)
admin.site.register(Servicios)
admin.site.register(user_profile)