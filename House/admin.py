from django.contrib import admin
from .models import *

admin.site.register(House)
admin.site.register(HouseImage)
admin.site.register(HousePaymentPeriod)
admin.site.register(HouseType)

# Register your models here.
