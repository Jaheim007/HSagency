from django.shortcuts import render
from Front.models import HouseSlide, SiteService
from customers.models import InfoAgent 
from House.models import LatestNews 

def index(request):
    datas = {
        "house_sliders": HouseSlide.objects.all(),
        "services": SiteService.objects.all(),
        "agents": InfoAgent.objects.all(),
        "latests_news": LatestNews.objects.all(),
    }
    return render(request,'pages/index.html', context=datas)
    

def about(request):
    return render(request,'pages/about.html')


def property(request):
    return render(request,'pages/property.html')

