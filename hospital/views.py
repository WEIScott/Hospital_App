from django.shortcuts import render
from Web_app.models import Hospital

# Create your views here.

#! write django function based views to pull all the data from hospital table.


def getHospitals(request):
	#! model query, get the data from the model.
	all_hospitals = Hospital.objects.all() #! select * from hospital_hospital
	return render(request, 'hospitals.html', {'all_hospitals_key':all_hospitals})


