from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.mypageIndex, name='mypage'),
    path('passwordUpdate/', views.passwordUpdate, name='passwordUpdate'),
    path('userinfoUpdate/', views.userinfoUpdate, name='userinfoUpdate'),
    path('userinfoUpdate/update/', views.userinfoUpdateUpdate, name='userinfoUpdateUpdate'),
    path('lecture/', views.lecture, name='lecture'),
    path('lectureDelete/', views.lectureDelete, name='lectureDelete'),
    path('mypageadmin/', views.mypageAdmin, name='mypageAdmin'),
    path('chat/chat_index/', views.chat_index, name='chat_index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    
]
