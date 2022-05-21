from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('about',views.about,name="about"),
    path('property',views.property,name="property"),
    path('contact',views.contact, name="contact"),
    path('blog',views.blog_grid, name="blog"),
    path('blog_single',views.blog_single, name="blog_single"),
    path('agent_single',views.agents_single, name="agent_single"),
    path('agent',views.agents_grid, name="agents"),
    path('property_grid',views.property_grid, name="property_grid"),
]