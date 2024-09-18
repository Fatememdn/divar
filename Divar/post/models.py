from django.db import models
from userapp.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=255)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.title


    

