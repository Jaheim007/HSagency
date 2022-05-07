from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    ADMIN = 'AD'
    CLIENT = 'CL'
    AGENT = 'AG'
    
    USER_TYPE = [
        (ADMIN,'admin'),
        (AGENT,'agent'),
        (CLIENT,'client')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dial_code = models.CharField(max_length=4)
    phone = models.CharField(max_length=10)
    image = models.URLField()
    birth_date = models.DateField(null=True, blank=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=255)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()
        
    def __str__(self):
        return self.user.username
        
class InfoAgent(models.Model):      
    customer = models.ForeignKey(Customer,  on_delete=models.CASCADE, related_name="customer_info_agent")
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
        return self.customer
    
    
# Create your models here.
