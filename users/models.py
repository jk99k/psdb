from enum import unique
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

import os
import uuid


class UserManager(BaseUserManager):

    def create_user(self, **request_data):
        user = self.model(**request_data)
        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        request_data = {
            'username': username,
            'email': email,
            'password': password
        }
        user = self.create_user(**request_data)
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    def get_user_icon_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), ext)
        return os.path.join('users/icons/', filename)

    CLIENT_CHOICES = [
        ('1', 'Smart Phone'),
        ('2', 'Tablet'),
        ('3', 'PC')
    ]

    # Basic
    username = models.CharField(unique=True, max_length=64)
    email = models.EmailField(unique=True)
    profile = models.CharField(blank=True, null=True, max_length=256)
    client = models.CharField(choices=CLIENT_CHOICES, max_length=2, default='1')
    icon = models.ImageField(upload_to=get_user_icon_path, blank=True, null=True)
 
    # PS3D profiles
    pixel_strike_id = models.IntegerField(blank=True, null=True)
    when_started = models.IntegerField(blank=True, null=True)

    # Core 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # Social accounts
    youtube_channel = models.CharField(blank=True, null=True, max_length=128)
    tiktok_account = models.CharField(blank=True, null=True, max_length=128)
    discord_account = models.CharField(blank=True, null=True, max_length=128)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAILFIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    @property
    def is_superuser(self):
        return self.is_admin

    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'Users'