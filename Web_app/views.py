from django.shortcuts import render
from patient.models import Patient
from .models import Hospital
from django.db.models import Q

# Create your views here.

def index(request):
	return render(request, 'index.html')


def all_model_queries(request):
	patients_agegreaterthan35=Patient.objects.filter(age__gt=35)
#! can write age__lt, age__eq, age__ne(not equal)
	age35query=patients_agegreaterthan35.query

	patient_fname_lname=Patient.objects.filter(
		Q(first_name__startswith='s') & Q(last_name__startswith='h')
		)
	search_fname_lname_query=patient_fname_lname.query

	context={
		'patients_agegreaterthan35_key':patients_agegreaterthan35,
		'age35query_key':age35query,

		'patient_fname_lname_key':patient_fname_lname,
		'search_fname_lname_query_key':search_fname_lname_query
	}
	return render(request, 'modelQueries.html', context)
