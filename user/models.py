from django.db import models
from django.contrib.auth.models import UserManager
from django.utils import timezone


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    tel = models.CharField(max_length=20, null=False, default='')
    role = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


class Post(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.ImageField(blank=True, upload_to='images', null=True)
    created_bd = models.DateTimeField(default=timezone.now)
    updated_bd = models.DateTimeField(default=timezone.now)
    show_ct = models.IntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('user.Post', on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_bd = models.DateTimeField(default=timezone.now)
    updated_bd = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author} :: {self.comment_text}'
