from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from .models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url = 'login')
def home(request):
	return render(request, 'core/home.html')


def sign_up(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit = False)
			user.set_password(form.cleaned_data['password'])
			user.save()
			return redirect('login')
	else:
		form = SignUpForm()
	return render(request, 'core/sign_up.html', {'form':form})


def view_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			try:
				user = authenticate(request, email = email, password = password )
				if user is not None:
					login(request, user)
					return redirect('home')
				else:
					error_message = 'Usuário ou Senha inválidos'
			except User.DoesNotExist:
				error_message = 'Usuário ou Senha inválidos'
		else:
			error_message = 'Usuário ou Senha inválidos'
	else:
		form = LoginForm()
		error_message = None
	return render(request, 'core/login.html', {'form': form, 'error_message': error_message})


@login_required
def view_logout(request):
	logout(request)
	return redirect('login')