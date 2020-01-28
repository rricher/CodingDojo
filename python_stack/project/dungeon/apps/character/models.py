from django.db import models
from ..user.models import User

class Character(models.Model):
    user = models.ForeignKey(User, related_name='characters', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    health = models.IntegerField()