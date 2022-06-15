from django.contrib import admin
from .models import InfoAgent, User, Testimonials

@admin.register(InfoAgent)
class Info(admin.ModelAdmin):
    list_display = ("user", 'Biographie', 'fb_link', 'insta_link', 'twitter_link', 'linkedin_link')

@admin.register(User)
class Custom(admin.ModelAdmin):
    list_display = ('username', 'dial_code', 'phone', 'image', 'birth_date', 'user_type')

@admin.register(Testimonials)
class Testimonials(admin.ModelAdmin):
    list_display = ("user", "message", "created")