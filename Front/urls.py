from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('about',views.about, name="about"),
    path('property',views.property, name="property"),
    path('property-single', views.property_single, name="property_single"),
]