from email.mime import image
from django.shortcuts import render
from . import models
from Front.models import HouseSlide 
from customers.models import InfoAgent 


def index(request):
    datas = {
        "house_sliders": HouseSlide.objects.all(),
        "services": models.SiteService.objects.all(),
        "agents": InfoAgent.objects.all(),
    }
    return render(request,'pages/index.html', context=datas)
    

def about(request):
    return render(request,'pages/about.html')


def property(request):
    return render(request,'pages/property.html')

