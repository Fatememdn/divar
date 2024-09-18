from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import random 

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    CITY_STATUS = (
        ('تهران', 'تهران'),
        ('اصفهان', 'اصفهان'),
        ('شیراز', 'شیراز'),
        ('مشهد', 'مشهد'),
        ('تبریز', 'تبریز'),
        ('کرمان', 'کرمان'),
        ('اهواز', 'اهواز'),
        ('رشت', 'رشت'),
        ('یزد', 'یزد'),
        ('کرمانشاه', 'کرمانشاه'),
        ('ارومیه', 'ارومیه'),
        ('قم', 'قم'),
        ('زاهدان', 'زاهدان'),
        ('اردبیل', 'اردبیل'),
        ('همدان', 'همدان'),
        ('بندرعباس', 'بندرعباس'),
    )
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("unknown", "Unknown"),
    )
    
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=11)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, choices=CITY_STATUS, blank=True, null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

