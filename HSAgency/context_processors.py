from Front.models import Contact
from House.models import HouseType, City

def info_contact(request):
    return {"contact": Contact.objects.first()}


def type_house(request):
    return {"list_type_house": HouseType.objects.all()}


def list_cities(request):
    return {"cities": City.objects.all()}
