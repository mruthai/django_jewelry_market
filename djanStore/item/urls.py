from django.urls import path
from . import views

app_name = 'item'

""" How urls are are captured by the user and their primary key and the item they are selling """
urlpatterns = [
    path('', views.items, name='items'), 
    path('new/', views.new_user_item, name='new_user_item'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    
]