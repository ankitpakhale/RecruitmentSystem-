from django.urls import path
from . import views

urlpatterns = [
    # for demo
    path('',views.hello, name='HELLO'),

    path('signup/',views.SignupView, name='SIGNUP'),
    path('login/', views.userLogin, name='LOGIN'),

    path('dash/', views.dashboard, name='DASHBOARD'),

    path('logout/', views.userLogOut, name='LOGOUT'), 

]