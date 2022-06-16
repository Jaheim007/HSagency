from Front.models import Contact

def info_contact(request):
    return {"contact": Contact.objects.first()}
