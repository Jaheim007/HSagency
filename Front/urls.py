from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "front_index"),
    path('about',views.about, name="front_about"),
    path('property',views.property, name="front_property"),
    path('property-single', views.property_single, name="property_single"),
]