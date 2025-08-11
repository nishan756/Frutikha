from django.shortcuts import render
from .models import Employee,OurPartner
from contact.models import Feedback
# Create your views here.

def AboutUs(request):
    employees = Employee.objects.all()
    feedbacks = Feedback.objects.all()
    partners = OurPartner.objects.all()
    return render(request,'about.html',{'employees':employees,'feedbacks':feedbacks,'partners':partners})

def Policies(request):
    return render(request,'policies.html')
