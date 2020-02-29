from django.db import models
from ..user.models import User

class ClassType(models.Model):
    name = models.CharField(max_length=45)
    start_hp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ability(models.Model):
    name = models.CharField(max_length=45)
    damage_min = models.IntegerField()
    damage_max = models.IntegerField()
    crit_chance = models.IntegerField()
    hit_chance = models.IntegerField()
    level_req = models.IntegerField()
    for_class = models.ForeignKey(ClassType, related_name="abilities", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Character(models.Model):
    user = models.ForeignKey(User, related_name='characters', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    max_hp = models.IntegerField()
    hp = models.IntegerField()
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    chosen_class = models.ForeignKey(ClassType, related_name='characters', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
