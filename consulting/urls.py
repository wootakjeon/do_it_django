from django.urls import path
from . import views

urlpatterns =[
    path('consulting/', views.consulting, name='consulting'),
    
]