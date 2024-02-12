from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat_data/', views.chat_data, name='chat_data'),
    path('mqtt/', views.mqtt, name='mqtt'),
]