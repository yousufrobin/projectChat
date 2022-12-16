from django import views
from django.contrib import admin
from django.urls import path, include
from Chat import views

urlpatterns = [
    path("", views.index, name="home"),
    path("checkview", views.checkview, name="checkview"),
    path("<str:room>/", views.room, name="room"),
    path("send", views.send, name="send"),
    path("getMessages/<str:room>/", views.getMessages, name="getMessages"),
]
