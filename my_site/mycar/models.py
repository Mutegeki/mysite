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
	"""docstring for Driver"""
	
		


      