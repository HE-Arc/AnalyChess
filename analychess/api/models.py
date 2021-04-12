from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'User : username {self.username}'
    
class Game(models.Model):
    owner = models.ManyToManyField(MyUser, related_name="games")
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    result = models.CharField(max_length=255, default="")
    moves = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'\n\tuser : {self.owner.all()}\n'
