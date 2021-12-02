from django.urls import path
from . import views


urlpatterns = [
	path('companies/', views.getCompanyData, name='insurancecompany'),
]