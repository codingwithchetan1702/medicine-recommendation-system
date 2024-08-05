from logging import _STYLES
from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse
from django.contrib import messages
from .models import Signup,Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# from rest_framework import status
from django.core.validators import RegexValidator, MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
from datetime import datetime
import requests
import json


def index(request): 
    return render(request,'index.html')

def feedback(request): 
    return render(request,'feedback.html')

def search(request): 
    return render(request,'search.html')

def contact(request):
    messages.success(request, "welcome to Contact page")
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact.name = name
        contact.email = email
        contact.desc = desc 

        contact.save()
        messages.success(
            request, " Your query has been successfully submitted")
    return render(request, 'contact.html')

# def Sign_up(request):
#     if request.method == 'POST':
#         Sign_up = Signup()
#         username = request.POST.get('username')
#         Email = request.POST.get('Email')
#         password = request.POST.get('password')
#         password2 = request.POST.get('repassword')
#         Sign_up.Username = username
#         Sign_up.Email = Email
#         Sign_up.password = password
        
#         # check for errorneous input

#         if (password != password2):
#             messages.error(request, "Passwords do not match")
#             return redirect('Sign_up')
#         else:
#             Sign_up.save()
#         # Create the user
#         myuser = User.objects.create_user(username, Email, password)
#         myuser.save()
#         messages.success(
#             request, " Your Account has been successfully created! login pleaser")
#         return redirect('login')
#     else:
#         return render(request,'sign_up.html')
    

def Sign_up(request):
    if request.method == 'POST':
        Sign_up = Signup()
        username = request.POST.get('username')
        email = request.POST.get('Email')
        password = request.POST.get('password')
        password2 = request.POST.get('repassword')
        m_no = request.POST.get('M_no')
        dob_str = request.POST.get('dob')
        gender = request.POST.get('gender')

        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()

        Sign_up.username = username
        Sign_up.email = email
        Sign_up.password = password
        Sign_up.m_no = m_no
        Sign_up.dob = dob
        Sign_up.gender = gender


        # Validate fields
        # email_validator = EmailValidator(message="Enter a valid email address")
        # mobile_validator = RegexValidator(regex=r'^\d{10}$', message='Mobile number must be exactly 10 digits')
        # password_validator = MinLengthValidator(8)

        
        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect('Sign_up')
        elif username == "":
            messages.error(request,"username is emp")
            return redirect('Sign_up')
        else:
            Sign_up.save()

    
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, "Your account has been successfully created! Please login.")
        return redirect('login')
    
    else:
        return render(request, 'sign_up.html')
    
def login(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        print(loginusername)
        loginpassword = request.POST['loginpassword']
        print(loginpassword)
        user = authenticate(username=loginusername, password=loginpassword)
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
             messages.error(request, "Invalid credentials! Please try again")
             return render(request, 'login.html')
    return render(request, 'login.html')
 
    # return HttpResponse("404- Not found")

    # return HttpResponse("login")


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("index")
    # return HttpResponse('handelLogout')

def about(request):
    return render(request,'about_us.html')

def news(request):
    messages.success(request, "welcome to News page") 
    # api_request = requests.get(
    #     "https://api.polygon.io/v2/reference/news?limit=10&order=descending&sort=published_utc&ticker=AAPL&published_utc.gte=2021-04-26&apiKey=XL5JZiyXF4aVL6zzsnVpp8jg4gYXp9ta")
    # api = json.loads(api_request.content)
    try:
        api_request = requests.get(
            "https://api.polygon.io/v2/reference/news?limit=10&order=descending&sort=published_utc&ticker=AAPL&published_utc.gte=2021-04-26&apiKey=XL5JZiyXF4aVL6zzsnVpp8jg4gYXp9ta")
        api_request.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        api = json.loads(api_request.content)
    except ConnectionError:
        messages.error(request, "Failed to establish a new connection. Please check your internet connection.")
        api = None
    except requests.exceptions.RequestException as e:
        messages.error(request, f"An error occurred: {e}")
        api = None
    return render(request, 'news.html', {'api': api, })

