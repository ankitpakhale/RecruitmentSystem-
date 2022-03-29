from django.urls import path
from . import views


app_name = 'app1'

urlpatterns = [
    path('hello/',views.hello, name='HELLO'),
    path('signup/',views.SignupView, name='SIGNUP'),
    path('login/', views.userLogin, name='LOGIN1'),
    path('dash/', views.dashboard, name='DASHBOARD'),
    path('logout/', views.userLogOut, name='LOGOUT'), 



    path('i1/', views.index1, name='index1'),
    path('i2/', views.index2, name='index2'),
    
    
    path('', views.home, name='HOME'),
    path('notfound/', views.notFound, name='NOTFOUND'), 
    path('about/', views.about, name='ABOUT'), 
    path('blogdetails/', views.blogDetails, name='BLOGDETAILS'), 
    path('blogfull/', views.blogFull, name='BLOGFULL'), 
    path('bloggrid/', views.blogGrid, name='BLOGGRID'), 
    path('blog/', views.blog, name='BLOG'), 
    path('candidatedetails/', views.candidateDetails, name='CANDIDATEDETAILS'), 
    path('candidateListing/', views.candidateListing, name='CANDIDATELISTING'), 
    path('companydetails/', views.companyDetails, name='COMPDETAILS'), 
    path('contact/', views.contact, name='CONTACT'),
    path('dashboard1/', views.dashboard1, name='DASHBOARD1'), 
    path('editprofile/', views.editProfile, name='EDITPROFILE'), 
    path('faqs/', views.faqs, name='FAQS'), 
    path('jobdetails/', views.jobDetails, name='JOBDETAILS'), 
    path('joblisting/', views.jobListing, name='JOBLISTING'), 

    path('packages/', views.packages, name='PACKAGES'), 
    path('postJob/', views.postJob, name='POSTJOB'), 
    path('register/', views.register, name='REGISTER'), 
    path('typography/', views.typography, name='TYPOGRAPHY'),
]