from django.shortcuts import render
from .forms import SignupForm

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
