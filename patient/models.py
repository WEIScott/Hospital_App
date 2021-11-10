from django.db import models


# Create your models here.
GENDER_CHOICES = [
	('M', 'MALE'),
	('F', 'FEMALE'),
	('O', 'OTHER') 
]

class Patient(models.Model):
	patient_id=models.IntegerField(primary_key=True)
	first_name=models.CharField("Patient`s First Name", max_length=200)
	last_name=models.CharField(max_length=200)
	slug=models.SlugField(max_length=50)
	age=models.PositiveIntegerField()
	gender=models.CharField(choices=GENDER_CHOICES, max_length=10)
	dateofbirth=models.DateField()
	mobile_number=models.CharField(max_length=20)
	email=models.EmailField()
	address=models.TextField()
	profileimage=models.ImageField(
		upload_to="images/patient/", null=True, blank=True)

	def __dtr__(self):
		return self.first_name + ' ' + last_name
		