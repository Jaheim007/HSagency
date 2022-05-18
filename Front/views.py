from email.mime import image
from django.shortcuts import render
from . import models

def index(request):
    datas = {
        "houses": models.House.objects.all(),
        "services": models.SiteService.objects.all(),
    }
    return render(request,'pages/index.html', context=datas)
    

def about(request):
    return render(request,'pages/about.html')


def property(request):
    return render(request,'pages/property.html')

