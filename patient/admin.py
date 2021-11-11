from django.contrib import admin
from .models import Patient

# Register your models here.


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	prepopulated_field = {'slug':('first_name', 'last_name'),}
	list_display = ['patient_id', 'profileimage', 'first_name', 'last_name', 
					'gender', 'age', 'mobile_number']
	list_filter = ['gender', 'first_name']