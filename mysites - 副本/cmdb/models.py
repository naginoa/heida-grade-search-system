from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(1, max_length=32)
    pwd = models.CharField(max_length=32)

class LogInfo(models.Model):
    user = models.CharField(max_length=32)
    tim = models.CharField(max_length=32)



