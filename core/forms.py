from django.forms import ModelForm
from django import forms
from .models import User


class SignUpForm(ModelForm):
	class Meta:
		model = User
		fields = ['name', 'email', 'password']
		widgets = {
			'name': forms.TextInput(
				attrs = {
					'type':'text',
					'id':"name",
					'name':"name",
					'placeholder':"Digite seu nome"
				}),
			'email': forms.TextInput(
				attrs = {
					"type":"email",
					"id":"email",
					"name":"email",
					"placeholder":"Digite seu email"
			}),
			'password': forms.TextInput(
				attrs = {
					"type":"password",
					"id":"password",
					"name":"password",
					"placeholder":"Digite sua senha"
			})}


	def save(self, commit = False):
		user = super(SignUpForm, self).save(commit = False)
		user.set_password(user.password)
		if commit:
			user.save()
		return user


class LoginForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(
		attrs={
			'class': 'email_input',
			'placeholder': 'Digite seu Email'
		}))
	password = forms.CharField(widget = forms.PasswordInput(
		attrs ={
			'placeholder': 'Digite sua Senha'
		}
		), max_length = 128)