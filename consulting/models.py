from django.db import models


# Create your models here.
class Consulting(models.Model):
    consulting_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    mentor_id = models.CharField(max_length=25)
    reg_date = models.DateTimeField(auto_now=True)
    mention = models.CharField(max_length=500)
    etc = models.CharField(max_length=500)
    update_mention = models.CharField(max_length=500, null=True)
