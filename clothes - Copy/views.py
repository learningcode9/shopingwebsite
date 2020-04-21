from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Sarees,Dresses,Lehangas,products



# Create your views here.

def home(request):
    
    return render(request,'Home.html')

def dresses(request):
    dresses=Dresses.objects.all()
    return render(request,'Dresses.html',{'dresses':dresses})

def sarees(request):
    sarees=Sarees.objects.all()
    return render(request,'saree.html',{'sarees':sarees})

def lehangas(request):
    lehangas=Lehangas.objects.all()
    return render(request,'Lehangas.html',{'lehangas':lehangas})

def add_to_cart(request):
    product=products.objects.all()
    return render(request,'checkout.html',{'product':product})

    

