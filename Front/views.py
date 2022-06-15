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
from House.models import LatestNews, House

def index(request):
    datas = {
        "house_sliders": HouseSlide.objects.all(),
        "services": SiteService.objects.all(),
        "agents": InfoAgent.objects.all(),
        "latests_news": LatestNews.objects.all(),
        "testimonials": Testimonials.objects.all(),
        "contact": Contact.objects.first(),
    }
    return render(request,'pages/index.html', context=datas)


def about(request):
    datas = {
        "teams": Team.objects.all(),
        "contact": Contact.objects.first(),
        "aboutsectiontwo": AboutSectionTwo.objects.first(),
        "aboutsectionone": AboutSectionOne.objects.first(),
    }
    return render(request,'pages/about.html', context=datas)


def property(request):
    return render(request,'pages/property.html', context={"houses": House.objects.all(),})

def property_single(request):
    return render(request,'pages/property-single.html')

