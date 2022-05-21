from email.mime import image
from django.shortcuts import render
from . import models

def index(request):
    
    return render(request,'pages/index.html')
    
def about(request):
    
    return render(request,'pages/about.html')

def property(request):
    
    return render(request,'pages/property.html')

def contact(request):
    
    return render(request,'pages/contact.html')

def blog_grid(request):
    
    return render(request,'pages/blog-grid.html')

def agents_grid(request):
    
    return render(request,'pages/agents-grid.html')

def agents_single(request):
    
    return render(request,'pages/agent-single.html')

def blog_single(request):
    
    return render(request,'pages/blog-single.html')

def property_grid(request):
    
    return render(request,'pages/property-grid.html')


# Create your views here.
