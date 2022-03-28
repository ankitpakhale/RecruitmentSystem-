from django.urls import path
from . import views


app_name = 'app1'

urlpatterns = [
    path('hello/',views.hello, name='HELLO'),

    path('signup/',views.SignupView, name='SIGNUP'),
    path('login/', views.userLogin, name='LOGIN'),
    path('', views.dashboard, name='DASHBOARD'),
    path('logout/', views.userLogOut, name='LOGOUT'), 
    
    path('home/', views.home, name='HOME'), 
    path('compdetails/', views.compDetails, name='CD'), 
]