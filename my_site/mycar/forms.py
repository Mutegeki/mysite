from django import forms
from. import models


class CreateCar(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = ['reg_no', 'year_of_manufacture',
                  'year_of_purchase', 'total_mileage_in_km']
