from django.contrib import admin
from .models import *

@admin.register(Slider)
class Slide(admin.ModelAdmin):
    list_display = (
        "title", 
        "contry", 
        "created", 
    )

@admin.register(SiteService)
class SiteService(admin.ModelAdmin):
    list_display = (
        "title", 
        "description", 
        "created",   
    )
