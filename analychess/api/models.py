from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'User : username {self.username}'
    
class Game(models.Model):
    owner = models.ManyToManyField(MyUser, related_name="games")
    path = models.CharField(max_length=255, unique=True)
    analyze_path = models.CharField(max_length=255, unique=True, default="null")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'\n\tuser : {self.owner.all()}\n\tpath : {self.path}\n\tanalyze_path : {self.analyze_path}\n'



