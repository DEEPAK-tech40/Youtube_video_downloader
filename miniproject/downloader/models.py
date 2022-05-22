from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.conf import settings

# Create your models here.


class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return username



class User_downloads(models.Model):
    user = models.ForeignKey(auth.models.User,on_delete=models.CASCADE,null=True)
    Video_downloaded = models.URLField()
    downloaded_on = models.DateTimeField(default=timezone.now)
