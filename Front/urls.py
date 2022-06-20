from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "front_index"),
    path('about/', views.about, name="front_about"),
    path('property/', views.property, name="front_property"),
    path('property/<int:property_id>/', views.PagePropertySingleGet.as_view(), name="front_property_single"),
    path('contact-agent/', views.PagePropertySinglePost.as_view(), name="front_contact_agent"),
]