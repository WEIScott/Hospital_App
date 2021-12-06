from django.shortcuts import render, redirect
from patient.models import Patient
from .models import Hospital
from django.db.models import Q, Avg,Max,Min,Sum, Count

from .forms import ContactModelForm
from django.http import HttpResponse

from user.forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
 
# Create your views here.

def index(request):
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
	return render(request, 'index.html', context )


def all_model_queries(request):
	patients_agegreaterthan35=Patient.objects.filter(
		age__gt=35).values('first_name', 'last_name')
#! can write age__lt, age__eq, age__ne(not equal)
	age35query=patients_agegreaterthan35.query


	patient_fname_lname=Patient.objects.filter(
		Q(first_name__startswith='e') & Q(last_name__startswith='h')
		)
	search_fname_lname_query=patient_fname_lname.query


	patient_firstname_exclude_e = Patient.objects.exclude(
		first_name__startswith='e')
	name_exclude_e_query=patient_firstname_exclude_e.query


	patient_nth_record = Patient.objects.order_by('-dateofbirth')[2]


	patient_avg_age = Patient.objects.all().aggregate(
		average_age=Avg('age'))


	patient_counts = Patient.objects.all().count()

	context={
		'patients_agegreaterthan35_key':patients_agegreaterthan35,
		'age35query_key':age35query,

		'patient_fname_lname_key':patient_fname_lname,
		'search_fname_lname_query_key':search_fname_lname_query,

		'patient_firstname_exclude_e_key':patient_firstname_exclude_e,
		'name_exclude_e_query_key':name_exclude_e_query,
		'patient_nth_record_key':patient_nth_record,

		'patient_avg_age_key':patient_avg_age,

		'patient_counts_key':patient_counts

	}
	return render(request, 'modelQueries.html', context)



def get_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			return HttpResponse('You data is submitted!')
	else:
		form = ContactForm()
	context = {
		'form_key': form
	}
	return render(request, 'get_contact.html', context) 


def ContactModelFormView(request):
	if request.method == 'POST':
		form = ContactModelForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('You data is submitted!')
	else:
		form = ContactModelForm()
	context = {
		'form_key': form
	}
	return render(request, 'get_contact.html', context) 


