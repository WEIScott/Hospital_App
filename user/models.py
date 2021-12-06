from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


GENDER_CHOICES = {
	('F', 'FEMALE'),
	('M', 'MALE')
}

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.IntegerField(blank=True, null=True)
	image = models.ImageField(blank=True, null=True, 
								upload_to="images/users/")
	bio = models.TextField(blank=True, null=True)
	gender = models.CharField(choices=GENDER_CHOICES, 
								max_length=10,blank=True, null=True)
	birthdate = models.DateField(default=datetime.now,
									blank=True, null=True)