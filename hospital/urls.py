from django.urls import path
from . import views


urlpatterns = [
	#! it takes 3 params: path`s name, views`s name, url`s name 
	path('', views.getHospitals, name='allhospitals'),

]