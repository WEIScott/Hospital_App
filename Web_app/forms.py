from django import forms
from .models import Contact


class ContactForm(forms.Form):
	name = forms.CharField(max_length=30, required=False)
	email = forms.EmailField()
	mobile = forms.IntegerField()


class ContactModelForm(forms.ModelForm):
	name = forms.CharField(label="Enter your name:", 
		widget=forms.TextInput(attrs={
			'class':'form-control'
		}
		))

	class Meta:
		model=Contact
		fields='__all__'
