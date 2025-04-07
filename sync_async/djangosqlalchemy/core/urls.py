# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sync/', views.sync_view, name='sync_view'),
    path('async/', views.async_view, name='async_view'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
]