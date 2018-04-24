# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
# Create your models here.
class Car(models.Model):
	reg_no=models.CharField(max_length=10, unique=True)
	year_of_manufacture=models.DateField()
	year_of_purchase=models.DateField()
	total_mileage_in_km=models.IntegerField()
	
	#def __str__(self):
	#	return self.reg_no


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
	

class Service(models.Model):
	distance = models.CharField(max_length=15)
	date = models.DateTimeField(auto_now_add=True)
	engine = models.CharField(max_length=10)
	engine = models.CharField(max_length=10)
	gear = models.CharField(max_length=10)
	diff = models.CharField(max_length=10)
	raditor = models.CharField(max_length=10)
	breaks = models.CharField(max_length=10)
	steering = models.CharField(max_length=10)
	battery = models.CharField(max_length=10)
	wind = models.CharField(max_length=10)
	air = models.CharField(max_length=10)
	spark = models.CharField(max_length=10)
	fuel = models.CharField(max_length=10)
	oil = models.CharField(max_length=10)
	flush = models.CharField(max_length=10)
	greasing = models.CharField(max_length=10)
	nexts = models.CharField(max_length=10)
	car = models.ForeignKey(Car)
	
		


      
