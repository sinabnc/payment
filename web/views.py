from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from . models import Card
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'web/index.html')

def login1(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get('pass')
        user = authenticate(request, username=username,password =password  )
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
             messages.warning(request,'invalid details')
             return redirect("login")
             
        
       


    return render(request,'web/login.html')

def singup(request):
    if request.method=="POST":
      username=request.POST.get("username")
      firstname=request.POST.get("lname")
      pass1=request.POST.get('pass')
      email=request.POST.get('email')

      if User.objects.filter(username=username).exists():
        messages.warning(request,'User already exist')
      else:
        user = User.objects.create_user(username,email, pass1)
        user.first_name=firstname
        user.save()
        return redirect('login')
    return render(request,'web/singup.html')


def logout1(request):
   logout(request)
   return redirect('index')

@login_required(login_url='login')
def price(request):
   return render(request,"web/price.html")

@login_required(login_url="login")
def deva(request):
   return render(request,'web/dev.html')

@login_required(login_url="login")
def card(request):
   


  
   if request.method=="POST":
      card = request.POST.get('card')
    
      

      if Card.objects.filter(card_number=card).exists() and Card.objects.filter(ex=card).exists() and Card.objects.filter(cvv=card).exists() :
         
     
        
         return redirect('index')
      else:
         return redirect("fal")
      
   return render(request,'web/cradit.html')


def fal(request):
   return render(request,"web/fal.html")