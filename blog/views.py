from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.timezone import datetime,timedelta
from django.core.mail import send_mail
# Create your views here.

def Blogs(request):
    search = request.GET.get('search')
    blogs = Blog.objects.all()
    if search:
        blogs = blogs.filter(Q(tital__icontains = search)|Q(detail__icontains = search))
    paginator = Paginator(blogs,6)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request,'blogs.html',{'blogs':page_obj})

def SingleBlog(request,id):
    blog = Blog.objects.get(id = id)
    recent_blogs = Blog.objects.filter(created_at__gte = datetime.now() - timedelta(days = 3),created_at__lte = datetime.today()).exclude(id = id)
    return render(request,'single-blog.html',{'blog':blog,'recent_blogs':recent_blogs})
