from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_post, name='add_post'),
    path('about/', views.about, name='about'),
    path('interests/', views.interests, name='interests'),
    path('delete/<int:id>', views.delete_post,name='delete'),
    path('edit/<int:id>', views.edit_post,name='edit'),
    path('comment/<int:id>', views.comment_post,name='comment'),
    path('current/<int:id>',views.current,name='current')
]

