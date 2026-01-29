from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=100)
    allow_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        default='avatars/default.png'
    )

    def __str__(self):
        return self.username
