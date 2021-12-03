from django.urls import path
from . import views


urlpatterns = [
		path('', views.index, name='index'),
		#!..url.path, views.function.name, url.name
		path('all_queries/', views.all_model_queries, name='allqueries'),
		path('post_contact/', views.get_contact, name='get_contact'),
		path('contactus/', views.ContactModelFormView, name='contactus'),
]