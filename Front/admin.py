from django.contrib import admin
from .models import (
    HouseSlide,
    SiteService,
    Contact,
    AboutSectionOne,
    AboutSectionTwo,
    Team
)

@admin.register(HouseSlide)
class Slide(admin.ModelAdmin):
    list_display = (
        "house_slide", 
        "date_created", 
    )

@admin.register(SiteService)
class SiteService(admin.ModelAdmin):
    list_display = (
        "title", 
        "description", 
        "date_created",   
    )
    
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = (
        "email", 
        "fb_link", 
        "insta_link",  
    )

@admin.register(AboutSectionOne)
class AboutSectionOne(admin.ModelAdmin):
    list_display = (
        "title_one", 
        "title_two", 
        "text",  
    )

@admin.register(AboutSectionTwo)
class AboutSectionTwo(admin.ModelAdmin):
    list_display = (
        "title_one", 
        "title_two", 
        "description",
    )

@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = (
        "first_name", 
        "last_name", 
        "description",  
    )