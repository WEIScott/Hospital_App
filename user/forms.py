from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class SignupForm(forms.ModelForm):
	username = forms.CharField(label="Enter your user account name:",
							help_text="Required. 150 characters or fewer.\
							Letters, digits and @/./+/-/_ only.",
							widget=forms.TextInput(attrs={
								'class':'form-control bg-light'
								})

		)
	first_name = forms.CharField(label="Enter your user account first name:",
							widget=forms.TextInput(attrs={
								'class':'form-control bg-light'
								})

		)
	last_name = forms.CharField(label="Enter your user account last name:",
							widget=forms.TextInput(attrs={
								'class':'form-control bg-light'
								})

		)
	email = forms.EmailField(label="Enter your email:",
							widget=forms.EmailInput(attrs={
								'class':'form-control bg-light'
								})

		)
	password = forms.CharField(label="Enter your password:",
							widget=forms.PasswordInput(attrs={
								'class':'form-control bg-light'
								})

		)


	class Meta:
		model = User
		fields= ['username', 'first_name',
				'last_name', 'email', 'password']