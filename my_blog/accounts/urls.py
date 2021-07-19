from django.urls import path, include
from . import views



urlpatterns = [
    
    path('register/', views.register,name='register'),
    path('loguserin/',views.loguserin,name='loguserin'),
    path('logout/',views.logout_view,name='logout_view')
]