from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.mypageIndex, name='mypage'),
    path('passwordUpdate/', views.passwordUpdate, name='passwordUpdate'),
    path('userinfoUpdate/', views.userinfoUpdate, name='userinfoUpdate'),
    path('userinfoUpdate/update/', views.userinfoUpdateUpdate, name='userinfoUpdateUpdate'),
    path('mypageadmin/', views.mypageAdmin, name='mypageAdmin')
]
