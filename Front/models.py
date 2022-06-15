from email.policy import default
from django.db import models
from django.utils.timezone import now
from House.models import House
from phonenumber_field.modelfields import PhoneNumberField


class SiteInfo(models.Model):     
    title = models.CharField(max_length=255)
    main_color = models.CharField(max_length=255)
    full_site_color = models.CharField(max_length=255)
    default_mode = models.BooleanField(default=True)
    
    date_created = models.DateTimeField(default=now())
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class Contact(models.Model): 
    fb_link = models.URLField()
    insta_link = models.URLField()
    twitter_link = models.URLField()
    linkedin_link = models.URLField()
    number_phone = PhoneNumberField()
    email = models.EmailField(max_length=50)
    
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5 , decimal_places=2)
    
    date_created = models.DateTimeField(default=now())
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
        
class HouseSlide(models.Model):
    """
    Cette class va permette d'éffectuer des CRUD sur les maisons

    Args:
        models (Model): Cette class nous permet de un models

    Returns:
        str : Elle nous retoune le titre de chaque instance crée
    """
    
    house_slide = models.ForeignKey(House, on_delete=models.CASCADE)
    photo_house = models.ImageField()
    date_created = models.DateTimeField(default=now())
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.house_slide.title

class SiteService(models.Model):
    """
    Cette class va permette d'éffectuer des CRUD sur les services
    de que propose l'agence sur la page d'index

    Args:
        models (Model): Cette class nous permet de un models_

    Returns:
        str : Elle nous retoune le titre de chaque instance crée
    """
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    photo_service = models.ImageField()
    
    date_created = models.DateTimeField(default=now())
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Page about
class AboutSectionOne(models.Model):
    title_one = models.CharField(max_length=255)
    title_two = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    photo = models.ImageField()
    
    created = models.DateTimeField(default=now())
    deleted = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    
class AboutSectionTwo(models.Model):
    title_one = models.CharField(max_length=255)
    title_two = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    photo = models.ImageField()
    
    created = models.DateTimeField(default=now())
    deleted = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    
class Team(models.Model):
    title = models.CharField(max_length=255, default='Exemple de titre')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    number_phone = PhoneNumberField()
    email = models.EmailField()
    fb_link = models.URLField(default="https://www.google.com/")
    instagram_link = models.URLField(default="https://www.google.com/")
    twitter_link = models.URLField(default="https://www.google.com/")
    linkedin_link = models.URLField(default="https://www.google.com/")
    photo = models.ImageField()
    
    created = models.DateTimeField(default=now())
    deleted = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    