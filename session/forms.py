from django import forms
from django.contrib.auth.forms import UserCreationForm
from .views import User

class CustomUserCreationForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].required = True
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2','email']
        widgets = {
            'email':forms.EmailInput(attrs = {'type':'email','placeholder':'Email'}),
            'username':forms.TextInput(attrs = {'type':'text','placeholder':'Username'}),
            'first_name':forms.TextInput(attrs = {'type':'text','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs = {'type':'text','placeholder':'Last Name'}),
            'password1':forms.PasswordInput(attrs = {'type':'password','placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs = {'type':'password','placeholder':'Rewrite password'}),

        }
        help_text = {
            'email':'Email is required to reset or change your password'
        }