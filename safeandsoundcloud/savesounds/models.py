from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


# Create your models here.
class User(AbstractUser, models.Model):
    # super().__init__(*args, **kwargs)
    username = models.CharField(max_length=200, unique=True)
    permalink = models.CharField(max_length=200)
    uri = models.CharField(max_length=400)
    permalink_url = models.CharField(max_length=400)
    avatar_url = models.CharField(max_length=400)
    access_token = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'username'

    def __string__(self):
        return self.username