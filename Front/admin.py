from django.contrib import admin
from .models import *

@admin.register(House)
class Slide(admin.ModelAdmin):
    list_display = (
        "title", 
        "contry", 
        "date_created", 
    )

@admin.register(SiteService)
class SiteService(admin.ModelAdmin):
    list_display = (
        "title", 
        "description", 
        "created",   
    )
