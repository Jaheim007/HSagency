from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('about',views.about,name="about"),
    path('property',views.property,name="property"),
    path('property_single',views.property_single,name="property_single"),
    path('blog',views.blog,name="blog"),
    path('blog_single',views.blog_single,name="blog_single"),
    path('agents', views.agents, name="agents"),
    path('contact', views.contact, name="contact"),
    path('agent_single', views.agent_single, name="agent_single"),
]