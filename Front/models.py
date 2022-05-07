from django.db import models

class SiteInfo(models.Model):     
    title = models.CharField(max_length=255)
    mainColor = models.CharField(max_length=255)
    fullSiteColor = models.CharField(max_length=255)
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
    
    created_at = models.DateTimeField()
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fb_link
        
class Slider(models.Model):
    title1 = models.CharField(max_length = 255)
    title2 = models.CharField(max_length = 255)
    title3 = models.CharField(max_length = 255)     
    image1 = models.URLField()
    image2 = models.URLField()
    image3 = models.URLField()
    
    created_at = models.DateTimeField()
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title1
    

# Create your models here.
