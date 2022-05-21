from django.contrib import admin
from .models import InfoAgent, User

@admin.register(InfoAgent)
class Info(admin.ModelAdmin):
    list_display = ('Biographie', 'fb_link', 'insta_link', 'twitter_link', 'linkedin_link')

@admin.register(User)
class Custom(admin.ModelAdmin):
    list_display = ('username', 'dial_code', 'phone', 'image', 'birth_date', 'user_type')
