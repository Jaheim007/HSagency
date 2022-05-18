from django.contrib import admin
from .models import *

@admin.register(Slider)
class Slide(admin.ModelAdmin):
    list_display = ('title','contry')



# Register your models here.
