from .views import Login,Logout,SignUp,ChangePassword
from django.urls import path

urlpatterns = [
    path('login/',Login,name = 'login'),
    path('logout/',Logout,name = 'logout'),
    path('signup/',SignUp,name = 'signup'),
    path('changepassword/',ChangePassword,name = 'changepassword'),
]