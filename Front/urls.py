from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "front_index"),
    path('about/', views.about, name="front_about"),
    path('properties/', views.property, name="front_property"),
    path('property/<int:property_id>/', views.PagePropertySingleGet.as_view(), name="front_property_single"),
    path('contact-agent/', views.PagePropertySinglePost.as_view(), name="front_contact_agent"),
    path('agent-grid/', views.front_agent_grid, name="front_agent_grid"),
    path('agent-single/<int:agent_id>/', views.front_agent_sinle, name="front_agent_single"),
    path('search-property/', views.SearchProperty.as_view(), name="front_search_property"),
]