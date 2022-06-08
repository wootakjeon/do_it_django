from django.db import models
from django.utils import timezone


# Create your models here.
class Chat_Propose(models.Model):
    email = models.ForeignKey('user.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    nickname = models.CharField(max_length=20, null=True)
    my_email = models.CharField(max_length=30)
    Parents_number = models.IntegerField()
    Mentor_number = models.IntegerField()
    created_bd = models.DateTimeField(default=timezone.now)
    updated_bd = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
