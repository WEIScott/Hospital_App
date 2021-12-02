from django.db import models

# Create your models here.


class Company(models.Model):
	insurancecompany_id=models.IntegerField(primary_key=True)
	insurancecompany_name=models.CharField(max_length=500)
	company_detail=models.TextField()


	def __str__(self):
		return self.insurancecompany_name

