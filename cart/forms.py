from .models import ConfirmOrder
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model = ConfirmOrder
        exclude = ['cart','created_at','total_price','products','order_status']
        widgets = {
            'name':forms.TextInput(attrs = {'type':'text','placeholder':'Name'}),
            'phone':forms.TextInput(attrs = {'type':'tel','placeholder':'Phone No'}),
            'location':forms.TextInput(attrs = {'type':'text','placeholder':'Location'}),

        }