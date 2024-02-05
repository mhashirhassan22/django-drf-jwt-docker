from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(verbose_name='Email Address', unique=True)

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.email
