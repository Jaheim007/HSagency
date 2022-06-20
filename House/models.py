from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.fields import CountryField
from customers.models import InfoAgent

class RealEstateType(models.Model):
    name = models.CharField(max_length=255)
    isactive = models.BooleanField(default=True) 
    description = models.TextField()
            
    date_created = models.DateTimeField(default=now())
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class HouseType(models.Model):
    type_category = models.CharField(max_length=225)
    
    date_created = models.DateTimeField(default=now())
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.type_category
    
class HousePaymentPeriod(models.Model):
    name = models.CharField(max_length=255)
    isactive = models.BooleanField(default=True)
    description = models.TextField(null=True) 
    symbol = models.CharField(max_length=2)
    
    date_created = models.DateTimeField(default=now())
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=150)
    
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    date_deleted = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class House(models.Model):
    info_agent = models.ForeignKey(InfoAgent, on_delete=models.CASCADE)  
    
    contry = CountryField(blank_label='(select country)')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE)
    beds = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=3)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000_000)])
    area = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000_000)])
    garage_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000_000)])
    rooms_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000_000)])
    toillete_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000_000)])
    latest_news_bool = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    main_image = models.ImageField()
    
    date_created = models.DateTimeField(default=now())
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    image = models.ImageField()
    
    created = models.DateTimeField(default=now)
    delete_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return str(self.house)           

class LatestNews(models.Model):
    info_agent = models.ForeignKey(InfoAgent, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    available_date = models.DateTimeField()
    
    date_created = models.DateTimeField(default=now())
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now=True)
    
class MessageAgent(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
    
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    date_deleted = models.DateTimeField(auto_now=True)