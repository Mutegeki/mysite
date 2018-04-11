# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render, redirect
from.models import Car, Driver, Service
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


#disabling csrf (cross site request forgery)
@csrf_exempt
def car_list(request):
	# if post request came
	if request.method == 'POST':
		try:
			car = Car(
				reg_no=request.POST['regno'],
				year_of_manufacture=request.POST['year_m'],
				year_of_purchase=request.POST['year_p'],
				total_mileage_in_km = request.POST['dist']
		    )
				#save them to the datadase
			car.save()
			#after saving them show
			context={
				'car':car
		    }
            # getting data from database
			#cars = Car.objects.all()
		except IntegrityError as e:
			print e
			context={'error':"its already exists"}
			return render(request,'car/car_list.html',{'cars':cars})

		    #getting our showcar template
  		
		return render(request,'car/showcar.html', context)
	else:
	    #if post request is not true 
	    #returing the form template
	    template = loader.get_template('car/car_list.html')
	return HttpResponse(template.render())


@csrf_exempt
def service(request):
	if request.method == 'POST':
		service = Service(
			distance=request.POST['distance'],
		)
		service.save()
		return render(request,'car/service.html', {'service':service})
	else:
	    template = loader.get_template('car/service.html')
	return HttpResponse(template.render())


@csrf_exempt
def car_detail(request, reg_no):
	#return HttpResponse(reg_no)
	car = Car.objects.get(reg_no=reg_no)
	if request.method == 'POST':
		service = Service(
			distance=request.POST['distance'],
		)
		service.save()
	return render(request, 'car/showcar.html', {'car': car})

@csrf_exempt
def driver(request):
	if request.method == 'POST':
		driver = Driver(
			first_name=request.POST['name'],
            last_name=request.POST['name1'],
            date_of_birth=request.POST['date'],
            sex=request.POST['sex'],
            phone_no=request.POST['phone'],
            permit=request.POST['permit'],
            nation=request.POST['nation'],
            district=request.POST['district'],
            #thumb=request.POST['file']
		)
		driver.save()
		drivers = Driver.objects.all()
		return render(request,'car/driverlist.html', {'drivers':drivers})

	else:
	    template = loader.get_template('car/driver.html')
	return HttpResponse(template.render())

def showcar_list(request):
	cars = Car.objects.all()
	drivers = Driver.objects.all()
	return render(request, 'car/showcar_list.html', {'cars': cars, 'drivers':drivers})
