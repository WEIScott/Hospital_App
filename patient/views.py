from django.shortcuts import render
from .models import Patient

# Create your views here.

def getAllPatients(request):
	all_patients = Patient.objects.all()
	context = {
		'all_patients_key':all_patients
	}
	return render(request, 'patient/all_patient.html', context)


def get_patient_info(request, patientid):
	the_patient=Patient.objects.filter(patient_id=patientid)
	context={
			'the_patient_key':the_patient
	}
	return render(request, 'patient/patient.html', context)