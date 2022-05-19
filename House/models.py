from django.db import models

class HouseType(models.Model): 
    name = models.CharField(max_length=255)
    isactive = models.BooleanField(default=True) 
    description = models.TextField(null=True)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class House(models.Model): 
    main_image = models.URLField()
    rooms_number = models.IntegerField()
    garage_number = models.IntegerField()
    toillete_number = models.IntegerField()
    address_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.agent
    
class HouseImage(models.Model):
    house = models.ForeignKey(House , on_delete=models.CASCADE , related_name="house_houseimage")
    image = models.URLField()
    
    created_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.house         
    

# Create your models here.
