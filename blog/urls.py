from django.urls import path
from .views import Blogs,SingleBlog

urlpatterns = [
    path('',Blogs,name = 'blogs'),
    path('single-blog/<str:id>/',SingleBlog,name = 'single-blog'),
]
