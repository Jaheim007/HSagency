from email.mime import image
from django.shortcuts import render
from . import models

def index(request):   
    slide = models.Slider.objects.filter().first()
    return render(request, 'index.html',locals() )  

def about(request):   
    return render(request, 'EstateAgency/EstateAgency/about.html')  

def agent_single(request):   
    return render(request, 'EstateAgency/EstateAgency/agents-single.html')  

def agents_grid(request):   
    return render(request, 'EstateAgency/EstateAgency/agents-grid.html')  

def blog_single(request):   
    return render(request, 'EstateAgency/EstateAgency/blog-single.html')  

def blog_grid(request):   
    return render(request, 'EstateAgency/EstateAgency/blog-grid.html')  

def contact(request):   
    return render(request, 'EstateAgency/EstateAgency/contact.html')  

def property_grid(request):   
    return render(request, 'EstateAgency/EstateAgency/property-grid.html')  

def property_single(request):   
    return render(request, 'EstateAgency/EstateAgency/property-single.html')  
 
    


# Create your views here.
