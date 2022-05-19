from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 'AD'
    CLIENT = 'CL'
    AGENT = 'AG'
    
    USER_TYPE = [
        (ADMIN,'admin'),
        (AGENT,'agent'),
        (CLIENT,'client')
    ]
    
    dial_code = models.CharField(max_length=4)
    phone = models.CharField(max_length=10)
    image = models.URLField()
    birth_date = models.DateField(null=True, blank=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=255)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.username
        
class InfoAgent(models.Model):      
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    Biographie = models.TextField(max_length=500)
    fb_link = models.URLField(blank=True , null=True)
    insta_link = models.URLField(blank=True , null=True)
    twitter_link = models.URLField(blank=True , null=True)
    linkedin_link = models.URLField(blank=True , null=True)
    whatsapp_number = models.CharField(blank=True , null=True, max_length=255)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user
    
    
# Create your models here.
