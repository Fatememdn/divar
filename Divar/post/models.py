from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField()
    author = models.OneToOneField(User)
    text = models.TextField()
    price = models.IntegerField()

    

