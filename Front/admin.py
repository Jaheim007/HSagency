from django.contrib import admin
from .models import *

@admin.register(Slider)
class Slide(admin.ModelAdmin):
    list_display = ('title1','title2','title3', 'image1', 'image2', 'image3')

@admin.register(Contact)
class ContactInfo(admin.ModelAdmin):
    list_display = ('fb_link','insta_link','twitter_link', 'linkedin_link', 'site_contact','dial_code','main_phone', 'email', 'latitude', 'longitude' )

@admin.register(SiteInfo)
class Site(admin.ModelAdmin):
    list_display = ('title', 'main_color', 'full_site_color', 'default_mode')

@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ('icon','service_name')


# Register your models here.
