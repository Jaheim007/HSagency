from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


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
    phone = PhoneNumberField()
    image = models.ImageField()
    birth_date = models.DateField(null=True, blank=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=255)
    
    created_at = models.DateTimeField(default=timezone.now)
    delete_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

class InfoAgent(models.Model):      
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    Biographie = models.TextField(max_length=500)
    fb_link = models.URLField(blank=True, null=True)
    insta_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    whatsapp_number = PhoneNumberField(blank=True, null=True)
    
    created = models.DateTimeField(default=timezone.now)
    delete_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username

    
