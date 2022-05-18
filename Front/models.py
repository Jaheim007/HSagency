from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django_countries.fields import CountryField

class SiteInfo(models.Model):     
    title = models.CharField(max_length=255)
    main_color = models.CharField(max_length=255)
    full_site_color = models.CharField(max_length=255)
    default_mode = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Contact(models.Model): 
    fb_link = models.URLField(null=True)
    insta_link = models.URLField(null=True)
    twitter_link = models.URLField(null=True)
    linkedin_link = models.URLField(null=True)
    site_contact = models.CharField(max_length=50) 
    main_phone = models.CharField(max_length=10) 
    dial_code = models.CharField(max_length=4)
    email = models.EmailField(max_length=50)  
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5 , decimal_places=2)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fb_link
        
class Slider(models.Model):
    contry = CountryField(blank_label='(select country)')
    city = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    photo_house = models.ImageField()
    created = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.title

class SiteService(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    photo_service = models.ImageField()
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

        
        
        
    