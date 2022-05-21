from django.contrib import admin
from .models import HouseSlide, SiteService

@admin.register(HouseSlide)
class Slide(admin.ModelAdmin):
    list_display = (
        "house_slide", 
        "created", 
    )

@admin.register(SiteService)
class SiteService(admin.ModelAdmin):
    list_display = (
        "title", 
        "description", 
        "created",   
    )
