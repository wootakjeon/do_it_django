from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mentor, name='mentor'),
    path('mentor_up/', views.mentor_up, name='upload_mento'),
    path('mentor_content/', views.mentor_content, name='mentor_content'),
    path('mentor_profile/', views.mentor_profile, name='mentor_profile'),
]