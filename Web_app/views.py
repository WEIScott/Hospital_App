from django.shortcuts import render
from patient.models import Patient
from .models import Hospital

# Create your views here.

def index(request):
	return render(request, 'index.html')


def all_model_queries(request):
	patients_agegreaterthan35=Patient.objects.filter(age__gt=35)
#! can write age__lt, age__eq, age__ne(not equal)
	context={
		'patients_agegreaterthan35_key':patients_agegreaterthan35
	}
	return render(request, 'modelQueries.html', context)
