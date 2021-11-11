from django.urls import path
from . import views


urlpatterns = [
	#! it takes 3 params: path`s name, views`s name, url`s name 
	path('allpatients/', views.getAllPatients, name='patients'),
	path('patient/<int:patientid>/', views.get_patient_info, name='the_patient_info')

]