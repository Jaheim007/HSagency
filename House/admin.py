from django.contrib import admin
from .models import *


@admin.register(House)
class HouseInfo(admin.ModelAdmin):
    list_display = ('agent', 'main_image', 'rooms_number', 'garage_number', 'toillete_number', 'address_name', 'price', 'price_payment', 'house_type', 'latitude', 'longitude')

@admin.register(HousePaymentPeriod)
class Period(admin.ModelAdmin):
    list_display = ('name', 'isactive', 'description', 'symbol')

@admin.register(HouseImage)
class Image(admin.ModelAdmin):
    list_display = ('house', 'image')

@admin.register(HouseType)
class Type(admin.ModelAdmin):
    list_display = ('name','isactive', 'description')


# Register your models here.
