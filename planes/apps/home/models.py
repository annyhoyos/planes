from django.db import models
from django.contrib.auth.models import User
from django.views.generic import TemplateView

class Hotel(models.Model):
	nombre     = models.CharField(max_length = 30)
	categoria  = models.CharField(max_length = 100) 
	habitacion = models.CharField(max_length = 100)
	

	

	def __unicode__ (self):
		return self.nombre

class Destino (models.Model):
	nombre = models.CharField(max_length = 100)
	Pais = models.CharField(max_length = 100)
	def __unicode__ (self):
		return self.nombre

class Transporte(models.Model):
	aereo     = models.CharField(max_length = 30)
	terrestre = models.CharField(max_length = 30)

	def __unicode__ (self):
		return self.aereo

class Descripcion(models.Model):
	incluye    = models.TextField(max_length = 500)
	no_incluye = models.TextField(max_length = 500)

	def __unicode__ (self):
		return self.incluye

class Servicios(models.Model):
	nombre = models.CharField(max_length = 500)

	def __unicode__ (self):
		return self.nombre

class Planes(models.Model):

	def url(self,filename):
		ruta = " MultimediaData/Planes/%s/%s"%(self.nombre, str(filename))
		return ruta
		
	nombre       = models.CharField(max_length = 100)
	descripcion  = models.TextField(max_length = 500)
	fecha_inicio = models.DateTimeField()
	fecha_fin    = models.DateTimeField()
	precio       = models.DecimalField(max_digits = 6, decimal_places = 3)
	imagen		 = models.ImageField(upload_to = url, null = True, blank =True) 
	hotel 		 = models.ManyToManyField(Hotel, null = True, blank = True)
	destino      = models.ManyToManyField(Destino,null = True, blank = True)
	transporte   = models.ManyToManyField(Transporte, null = True, blank = True)
	descripcion  = models.ManyToManyField(Descripcion, null = True, blank = True)
	

	def __unicode__ (self):
		return self.nombre

class user_profile(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Users/%s/%s"%(self.user.username.filename)
		return ruta

	user 		= models.OneToOneField(User)
	photo		= models.ImageField(upload_to=url)
	telefono	= models.CharField(max_length=30)

	def __unicode__(self):
		return self.user.username

class BuscarView(TemplateView):

	def post(self, request, *args, **Kwargs):
		buscar = request.POST['buscalo'] 
		busqueda = planes.objects.filter(nombre__icontains=buscar)  
		if busqueda:  
			ctx = {'planes':busqueda}
			return render(request, 'home/busqueda.html', ctx) 
		else: 
			info = ("articulo no encontrado")
			ctx = {'planes':busqueda}
			return render(request, 'home/busqueda.html', info)


# Create your models here.
