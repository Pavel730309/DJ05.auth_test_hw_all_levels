from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField("Номер телефона", max_length=15, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
