import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class AppUserManager(BaseUserManager):
    def _create_user(self, username, password=None, is_superuser=False, **kwargs):
        user = self.model(username=username, is_superuser=is_superuser, **kwargs)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password=None, **kwargs):
        return self._create_user(username, password, is_superuser=False, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        return self._create_user(username, password, is_superuser=True, **kwargs)


class AppUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=50, unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True)
    birthday = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')
    date_joined = models.DateTimeField(default=timezone.now)

    objects = AppUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ('first_name', 'last_name', )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_staff(self):
        return self.is_superuser
