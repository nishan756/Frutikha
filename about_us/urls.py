from .views import AboutUs,Policies
from django.urls import path

urlpatterns = [
    path('',AboutUs,name = 'about_us'),
    path('policies/',Policies,name = 'policies'),
]
