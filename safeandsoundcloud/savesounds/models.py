from django.db import models


# Create your models here.
class User(models.Model):
    # super().__init__(*args, **kwargs)
    username = models.CharField(max_length=200)
    permalink = models.CharField(max_length=200)
    uri = models.CharField(max_length=400)
    permalink_url = models.CharField(max_length=400)
    avatar_url = models.CharField(max_length=400)
    access_token = models.CharField(max_length=100, blank=True)

    def __string__(self):
        return self.username



class AccessToken(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100, default=None)
    # expires = models.DateTimeField()
    # scope = models.CharField(max_length=50)

    def __string__(self):
        return self.access_token
