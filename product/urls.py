from .views import AllProduct,SingleProduct
from django.urls import path

urlpatterns = [
    # Home url located in main url.py
    path('all-product/',AllProduct,name = 'all-product'),
    path('single-product/<str:id>/',SingleProduct,name = 'single-product'),

]
