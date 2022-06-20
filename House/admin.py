from django.contrib import admin
from .models import (
    House,
    HousePaymentPeriod,
    HouseImage,
    HouseType,
    RealEstateType,
    LatestNews,
    City,
    MessageAgent,
)


@admin.register(House)
class HouseInfo(admin.ModelAdmin):
    list_display = (
        'info_agent',
        'main_image',
        'rooms_number',
        'garage_number',
        'toillete_number',
        'price',
        'house_type',
        'latitude',
        'longitude',
        'city',
    )
    

@admin.register(HousePaymentPeriod)
class Period(admin.ModelAdmin):
    list_display = (
        'name',
        'isactive',
        'description',
        'symbol'
    )

@admin.register(HouseImage)
class Image(admin.ModelAdmin):
    list_display = (
        'house',
        'image'
    )

@admin.register(HouseType)
class HouseType(admin.ModelAdmin):
    list_display = (
        "type_category",
    )

@admin.register(RealEstateType)
class RealEstateType(admin.ModelAdmin):
    list_display = (
        'name',
        'isactive',
        'description' 
    )
    
@admin.register(LatestNews)
class LatestNews(admin.ModelAdmin):
    list_display = (
        'info_agent',
        'message',
        'available_date' 
    )
    
@admin.register(City)
class Ciry(admin.ModelAdmin):
    list_display = (
        'name',
    )
    
@admin.register(MessageAgent)
class MessageAgent(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'message',
    )
