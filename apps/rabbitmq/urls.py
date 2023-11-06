from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('send-message/', views.send_message, name='send_message'),
    path('receive-messages/', views.receive_messages, name='receive_messages'),
]