from django.urls import path, include
from . import views

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
    path('join_select/',views.join_select, name ='join_select'),
    path('join_mentor/',views.join_mentor, name ='join_mentor'),
    path('join_mentee/',views.join_mentee, name ='join_mentee'),
    path('community',views.community, name='community'),
    path('new_writing/',views.new_writing, name = 'new_writing'),
    path('community_post/',views.community_post,name='community_post'),
    path('logout/', views.logout, name='logout'),
    path('cover_letter/',views.cover_letter,name='cover_letter'),
    path('mypost/',views.mypost,name='mypost'),
]


