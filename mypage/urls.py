from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.mypageIndex, name='mypage'),
    path('mypageadmin/', views.mypageAdmin, name='mypageAdmin')
]
