from ast import Num
from email.headerregistry import Address
from platform import uname
from unicodedata import category
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from . models import *
from django.http import HttpResponse
from django.contrib import messages

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
        
        details = studentData.objects.all()
        print(details)
        
        return render(request,'dashboard.html', {'name': name, 'student': student, 'details': details})
    return redirect('LOGIN')

def userLogOut(request):
    del request.session['email']
    print('User logged out successfully')
    return redirect('LOGIN')