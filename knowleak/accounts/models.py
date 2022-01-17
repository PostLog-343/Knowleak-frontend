from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, password,email, first_name,last_name,**other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_teacher', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, last_name, password, **other_fields)

    def create_user(self,  email, username, first_name,last_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))
        if not password:
            raise ValueError(_('You must provide a password.'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name,last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user



class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    email = models.EmailField(_('email address'), unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    token = models.IntegerField(default=0)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    
    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username