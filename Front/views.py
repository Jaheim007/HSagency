from email.mime import image
from django.shortcuts import render
from . import models

def index(request):
    
    return render(request,'pages/index.html')
    

def about(request):
    
    return render(request,'pages/about.html')


def property(request):
    
    return render(request,'pages/property.html')

# Create your views here.
