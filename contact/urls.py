from .views import ContactUs
from django.urls import path

urlpatterns = [
    # Subscribe url located in main url.py
    path('',ContactUs,name = 'contact_us'),
]
