from pprint import pprint
from django.shortcuts import render
from Front.models import (
    HouseSlide,
    SiteService,
    Contact,
    AboutSectionTwo,
    AboutSectionOne,
    Team,
)
from customers.models import InfoAgent, Testimonials
from House.models import LatestNews, House, HouseImage


def index(request):
    datas = {
        "house_sliders": HouseSlide.objects.all(),
        "services": SiteService.objects.all(),
        "agents": InfoAgent.objects.all(),
        "latests_news": LatestNews.objects.all(),
        "testimonials": Testimonials.objects.all(),
    }
    return render(request,'pages/index.html', context=datas)


def about(request):
    datas = {
        "teams": Team.objects.all(),
        "aboutsectiontwo": AboutSectionTwo.objects.first(),
        "aboutsectionone": AboutSectionOne.objects.first(),
    }
    return render(request,'pages/about.html', context=datas)

 
def property(request):
    return render(request,'pages/property.html', context={"houses": House.objects.all(),})


def property_single(request, property_id):
    house = HouseSlide.objects.get(id=property_id)
    photos = HouseImage.objects.filter(house=house.house_slide)
    
    return render(request,'pages/property-single.html', context={"house": house, "photos": photos})
