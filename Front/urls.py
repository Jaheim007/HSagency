from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('agentSingle',views.agent_single, name='agentSingle'),
    path('agentGrid',views.agents_grid, name='agentGrid'),
    path('blog',views.blog_grid, name='blog'),
    path('blogSingle',views.blog_single, name='blogSingle'),
    path('property',views.property_grid, name='property'),
    path('propertySingle',views.property_single, name='propertySingle'),
    path('contact',views.contact, name='contact'),
    path('about',views.about, name='about'),
]