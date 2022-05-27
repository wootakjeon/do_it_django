from django.urls import path, include
from . import views

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
    path('logout/', views.logout, name='logout'),
    path('board/', views.board, name='board'),
    path('board/board_write/', views.board_write, name='board_write'),
    path('board/board_detail/<int:boardid>/', views.board_detail, name='board_detail')
]