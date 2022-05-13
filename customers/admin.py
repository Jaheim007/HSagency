from django.contrib import admin
from .models import *


class Info(admin.ModelAdmin):
    list_display = ('customer', 'Biographie', 'fb_link', 'insta_link', 'twitter_link', 'linkedin_link')

admin.site.register(InfoAgent, Info )

class Custom(admin.ModelAdmin):
    list_display = ('user', 'dial_code', 'phone', 'image', 'birth_date', 'user_type')

admin.site.register(Customer, Custom)


# Register your models here.
