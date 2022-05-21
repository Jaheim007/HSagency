from email.mime import image
from django.shortcuts import render
from . import models

def index(request):
    home = True
    return render(request,'pages/index.html', locals())
#---------------views about-----------------#     
def about(request):
    about= True
    return render(request,'pages/about.html', locals())

#---------------views property-----------------#  
def property(request):
    property = True
    return render(request,'pages/property.html', locals())

def property_single(request):
    
    return render(request,'pages/property-single.html', locals())
#----------------views  blog-------------------#  

def blog(request):
    blog = True
    return render(request,'pages/blog.html', locals())

def blog_single(request):
    
    return render(request,'pages/blog-single.html', locals())
#---------------views agents-----------------#    
def agents(request):
    return render(request, "pages/agents.html")

#---------------views contacts-----------------#  
def contact(request):
    contact = True
    return render(request, "pages/contact.html", locals())

#------------views agent-single--------------#  
def agent_single(request):
    return render(request, "pages/agent-single.html")

# Create your views here.
