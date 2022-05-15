from django.db import models


# Create your models here.
class UserInfo(models.Model):
    email = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    role = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
