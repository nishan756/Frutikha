from django.shortcuts import render
from .models import Product
from django import http
from django.db.models import Q
from django.core.paginator import Paginator
from blog.models import Blog
from contact.models import Feedback
# Create your views here.



def get_product(id):
    try:
        return Product.objects.get(id = id)
    except Product.DoesNotExist:
        return None

def Home(request):
    blogs = Blog.objects.all()[:5]
    products = Product.objects.all()[:6]
    feedbacks = Feedback.objects.all()[:5]
    return render(request,'index.html',{'blogs':blogs,'products':products,'feedbacks':feedbacks})

def AllProduct(request):
    # Search 
    search = request.GET.get('search')
    # Products
    products = Product.objects.all()
    if search:
        products = products.filter(Q(name__icontains = search))
    paginator = Paginator(products,10)
    page_num = request.GET.get('page')
    page_objs = paginator.get_page(page_num)
    return render(request,'all-product.html',{'products':page_objs})

def SingleProduct(request,id):
    product = get_product(id)
    if product:
        return render(request,'single-product.html',{'product':product})
    else:
        return render(request,'404.html',{'message':'Product not found'})


