from django import forms
from .models import Contact


class ContactForm(forms.Form):
	name = forms.CharField(max_length=30, required=False)
	email = forms.EmailField()
	mobile = forms.IntegerField()


class ContactModelForm(forms.ModelForm):
	name = forms.CharField(label="Enter your name:", 
		help_text='This is the help message, 100 characters max',
		widget=forms.TextInput(attrs={
			'class':'form-control'
		}))
	email = forms.EmailField(label="Enter your Email:",
		widget=forms.EmailInput(attrs={
			'class':'form-control'
			}))
	message = forms.CharField(
		label="Leave us a message:",
		widget=forms.Textarea(attrs={
			'class':'form-control'
			}))

	class Meta:
		model=Contact
		fields='__all__'
