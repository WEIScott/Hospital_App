from django.urls import path
from . import views

urlpatterns = [
	path('claims/', views.ClaimData, name='claimdata'),
]