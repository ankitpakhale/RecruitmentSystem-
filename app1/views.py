from ast import Num
from email.headerregistry import Address
from platform import uname
from unicodedata import category
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from . models import *
from django.http import HttpResponse
from django.contrib import messages

from django.db.models.query_utils import Q

# Create your views here.

def hello(request):
    return HttpResponse("You are in school recruitment system................")

def SignupView(request):
    if request.POST: 
        Name = request.POST['name']
        Email = request.POST['email']
        Number = request.POST['number']
        Address = request.POST['address']
        Password = request.POST['password']
        ConfirmPassword = request.POST['confirmPassword']
        Category = request.POST['cat']
        print(Category)
        try:
            data = signUp.objects.filter(email=Email)
            if data:
                msg = "Email already registered"
                return render(request, 'signup.html', {'msg': msg})
            elif ConfirmPassword == Password:
                v = signUp()
                v.name = Name
                v.email = Email
                v.number = Number
                v.address = Address
                v.password = Password
                if Category == 'rec':
                    Category = 0
                    v.isStu = Category
                else:
                    Category = 1
                    v.isStu = Category
                v.save()
                print(f"{v.name} Signed up successfully")
                return redirect('LOGIN')
            else:
                msg = 'Please Enter Same Password'
                return render(request , 'signup.html',{'msg':msg}) 
        finally:
            messages.success(request, 'Signup Successfully Done...')
    return render(request,'signup.html')

def userLogin(request):
    if request.POST:
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
      
        print("Inside first try block", em)
        check = signUp.objects.get(email = em)
        print("Email is ",em)
        if check.password == pass1:
            request.session['email'] = check.email
            print(f'{check.name} Successfully logged in')
            return redirect('DASHBOARD')
        else:
            return HttpResponse('Invalid Password')
    return render(request,'login.html')


def dashboard(request):
    if 'email' in request.session:
        name = signUp.objects.get(email = request.session['email'])
        
        student = name.isStu
        print(f"{name} is {student}")
        print(type(student))
        
        if request.POST: 
            # saving data in database
            data = studentData()
            data.name = request.POST['name']
            data.email = request.POST['email']
            data.city = request.POST['city']
            data.dob = request.POST['dob']
            data.uname = request.POST['uname']
            data.cname = request.POST['cname']
            data.pyear = request.POST['pyear']
            data.spi = request.POST['spi']
            data.pl = request.POST['pl']
            data.description = request.POST['description']
            data.save()
            print("Data Successfully Submitted")
            return HttpResponse("Data Successfully Submitted")
        
        details = studentData.objects.all()

        # search module start
        print("Inside search module")
        s = request.GET.get('search')
        print(s)
        if s:
            q = studentData.objects.filter(Q(name__icontains = s) | Q(email__icontains = s) | Q(city__icontains = s) | Q(dob__icontains = s) | Q(uname__icontains = s) | Q(cname__icontains = s) | Q(pyear__icontains = s) | Q(spi__icontains = s) | Q(pl__icontains = s) | Q(description__icontains = s))
        else:
            q = details
        print(q)
        return render(request,'dashboard.html', {'name': name, 'student': student, 'details': details, 's':q})
    return redirect('LOGIN')

def userLogOut(request):
    del request.session['email']
    print('User logged out successfully')
    return redirect('LOGIN')


def home(request):
    return render(request,'index3.html')

def notFound(request):
    return render(request,'404.html')

def about(request):
    return render(request,'about-us.html')

def blogDetails(request):
    return render(request,'blog-detail.html')

def blogFull(request):
    return render(request,'blog-full-width.html')

def blogGrid(request):
    return render(request,'blog-grid.html')

def blog(request):
    return render(request,'blog.html')

def candidateDetails(request):
    return render(request,'candidate-detail.html')

def candidateListing(request):
    return render(request,'candidate-listing.html')

def companyDetails(request):
    return render(request,'company-detail.html')

def contact(request):
    return render(request,'contact-us.html')

def dashboard1(request):
    return render(request,'dashboard1.html')

def editProfile(request):
    return render(request,'edit-profile.html')

def faqs(request):
    return render(request,'faqs.html')

def jobDetails(request):
    return render(request,'job-detail.html')

def jobListing(request):
    return render(request,'job-listing.html')

def login1(request):
    return render(request,'login1.html')

def packages(request):
    return render(request,'packages.html')

def postJob(request):
    return render(request,'post-job.html')

def register(request):
    return render(request,'register.html')

def typography(request):
    return render(request,'typography.html')
