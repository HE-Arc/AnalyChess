# Generated by Django 3.1.7 on 2021-03-05 15:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20210305_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='owner',
        ),
        migrations.AddField(
            model_name='game',
            name='owner',
            field=models.ManyToManyField(related_name='games', to=settings.AUTH_USER_MODEL),
        ),
    ]