from Front.models import Contact,SiteInfo

def Contact(request):    
    contact = Contact.objects.get()
    
    return  {
        'contact': contact
    }