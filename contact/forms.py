from .models import Contact
from django import forms

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs = {'type':'text','placeholder':'Your Name','id':'name'}),
            'phone':forms.TextInput(attrs = {'type':'text','placeholder':'Your Cell','id':'phone'}),
            'email':forms.EmailInput(attrs = {'type':'email','placeholder':'Your Email','id':'email'}),
            'subject':forms.TextInput(attrs = {'type':'text','placeholder':'Subject','id':'subject'}),
            'message':forms.Textarea(attrs = {'type':'teat','placeholder':'Write Message','cols':30,'rows':10,'id':'message'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')

        if not phone and not email:
            raise forms.ValidationError('You must fill up either the email or phone field.')

        return cleaned_data

    
