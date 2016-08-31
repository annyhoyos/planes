from django import forms
from planes.apps.home.models import Planes, Hotel, Destino, Transporte, Descripcion, Servicios
from django.contrib.auth.models import User


class add_planes_form(forms.ModelForm):
	class Meta:
		model   = Planes

		exclude  = {'status',}

class add_hotel_form(forms.ModelForm):
	class Meta:
		model   = Hotel

		
class add_destino_form(forms.ModelForm):
	class Meta:
		model   = Destino

	

class add_transporte_form(forms.ModelForm):
	class Meta:
		model   = Transporte

		exclude  = {'status',}

class add_descripcion_form(forms.ModelForm):
	class Meta:
		model   = Descripcion

class add_servicios_form(forms.ModelForm):
	class Meta:
		model   = Servicios




class login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())
	clave   = forms.CharField(widget = forms.PasswordInput(render_value = False))

class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
	email 	 = forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
	password_one = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')




