from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from customers.models import InfoAgent 
from django_countries.fields import CountryField


class HouseType(models.Model): 
    name = models.CharField(max_length=255)
    isactive = models.BooleanField(default=True) 
    description = models.TextField(null=True)
    
    created = models.DateTimeField(default=timezone.now())
    delete_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.name
    
class HousePaymentPeriod(models.Model):
    name = models.CharField(max_length=255)
    isactive = models.BooleanField(default=True)
    description = models.TextField(null=True) 
    symbol = models.CharField(max_length=2)
    
    created = models.DateTimeField(default=timezone.now())
    delete_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True) 
    
    def __str__(self):
        return self.name
       
class House(models.Model): 
    info_agent = models.ForeignKey(InfoAgent, on_delete=models.CASCADE)  
    
    contry = CountryField(blank_label='(select country)')
    city = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000_000)])
    area = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000_000)])
    garage_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000_000)])
    rooms_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000_000)])
    toillete_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000_000)])
    
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE)
    main_image = models.ImageField()
    
    created = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return str(self.title)
    
class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    image = models.URLField()
    
    created = models.DateTimeField(default=timezone.now())
    delete_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
        
    def __str__(self):
        return self.house         

