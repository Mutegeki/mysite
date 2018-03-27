# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Car(models.Model):
	reg_no=models.CharField(max_length=10, unique=True)
	year_of_manufacture=models.DateField()
	year_of_purchase=models.DateField()
	total_mileage_in_km=models.IntegerField()



	#def __str__(self):
		#return self.


class Driver(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	date_of_birth=models.DateField()
	sex=models.CharField(max_length=10)
	phone_no=models.CharField(max_length=13, unique=True)
	permit=models.CharField(max_length=40, unique=True)
	nation=models.CharField(max_length=15)
	district=models.CharField(max_length=30)
	#thumb=models.ImageField(default='default.png',blank=True)
	

	

		


      