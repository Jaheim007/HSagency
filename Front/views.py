import re
import json
from Front.models import (
    HouseSlide,
    SiteService,
    Contact,
    AboutSectionTwo,
    AboutSectionOne,
    Team,
)
from customers.models import InfoAgent, Testimonials
from House.models import (
    LatestNews,
    House,
    HouseImage,
    MessageAgent
)
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

# Page property single000
class PagePropertySingleGet(View):
    def get(self, request, property_id):
        house = HouseSlide.objects.get(id=property_id)
        photos = HouseImage.objects.filter(house=house.house_slide)
        
        return render(request,'pages/property-single.html', context={"house": house, "photos": photos})
    
class PagePropertySinglePost(View):
    def get(self, request):
        return redirect("front_index")
     
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        if (
            name 
            and not name.isspace()
            and message
            and not message.isspace()
            and re.search(regex, email)
        ):
            print(email)
            MessageAgent.objects.create(name=name, email=email, message=message)
            return HttpResponse(headers={
                "HX-Trigger": json.dumps({
                    "showMessage": {
                        "icon": "success",
                        "title": "Prise de contact avec l'argent",
                        "message": "Vôtre message a bien été envoyé"
                    }
                }
                ) 
            })
        return HttpResponse(headers={
            "HX-Trigger": {
                "showMessage": {
                    "icon": "error",
                    "title": "Echec de la prise de contact avec l'argent",
                    "message": "Vôtre message n'a été envoyé cas une erreur est suvénu"
                }
            }
        })
       

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
     
        
def front_agent_grid(request):
    return render(request,'pages/agents-grid.html', context={"agents": InfoAgent.objects.all(),})
     
     
def front_agent_sinle(request, agent_id):
    agent = InfoAgent.objects.get(id=agent_id)
    houses = House.objects.filter(info_agent=agent_id)
    return render(request,'pages/agent-single.html', context={"agent": agent, "houses": houses})
     
        
