from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_post, name='add_post'),
    path('about/', views.about, name='about'),
    path('interests/', views.interests, name='interests'),
]

