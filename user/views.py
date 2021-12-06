from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def signup_view(request):
	if request.method == 'POST':
		signupform = SignupForm(request.POST)
		if signupform.is_valid():
			signupform.save()
			return HttpResponse('You`ve been sign up successively!')
	else:
		signupform = SignupForm()
	context = {
		'signupform_key':signupform
	}
	return render(request, 'users/registration.html', context)


def login_view(request):
	if request.method == 'POST':
		loginform = LoginForm(request.POST)
		uname = request.POST.get("username")
		password = request.POST.get("password")
		user_data = authenticate(username=uname, password=password)
		print('user data is: ', user_data)
		if user_data is not None:
			login(request, user_data)
			return redirect('claimdata')
		else:
			messages.error(request, 'User or password is incorrect')
	else:
		loginform = LoginForm()
	context = {
		'loginform_key':loginform
	}
	#url_path = ['user/login.html', 'index.html']
	return render(request, 'users/login.html', context)



def logout_view(request):
	logout(request)
	return redirect('index')

