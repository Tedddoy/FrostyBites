from django import forms
from .models import User
from .models import Services



class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['service_name', 'details', 'price']

