from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', default='default_user_photo.png', blank=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['username']
        verbose_name_plural = 'users'

    def __str__(self):
        return f'{self.username} - {self.uuid}'
