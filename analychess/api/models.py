from django.db import models

# Create your models here.

class Game(models.Model):
    owner = models.ManyToManyField('auth.User', related_name='games')
    path = models.CharField(max_length=255, unique=True)
    analyze_path = models.CharField(max_length=255, unique=True, default="null")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'\n\tuser : {self.owner.all()}\n\tpath : {self.path}\n\tanalyze_path : {self.analyze_path}\n'

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



