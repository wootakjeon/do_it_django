from django.db import models


# Create your models here.
class Mentor(models.Model):
    email = models.ForeignKey('user.User', on_delete=models.CASCADE)
    mentor = models.CharField(max_length=30)
    mentor_img = models.ImageField(upload_to='images/')
    mento_title = models.CharField(max_length=100)
    mento_content = models.CharField(max_length=5000)
    mento_field = models.CharField(max_length=50)

    def __str__(self):
        return self.mento_title
