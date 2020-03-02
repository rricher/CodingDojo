from django.db import models
from ..character.models import Character

class Monster(models.Model):
    _type = models.CharField(max_length=45)
    # if _type == "Goblin":
    #     name = models.CharField(max_length=45, default="Goblin")
    #     max_hp = models.IntegerField(default=20)
    #     hp = models.IntegerField(default=20)
    #     damage_min = models.IntegerField(default=2)
    #     damage_max = models.IntegerField(default=4)
    #     exp = models.IntegerField(default=5)
    # elif _type == "Slime":
    #     name = models.CharField(max_length=45, default="Slime")
    #     max_hp = models.IntegerField(default=15)
    #     hp = models.IntegerField(default=15)
    #     damage_min = models.IntegerField(default=1)
    #     damage_max = models.IntegerField(default=2)
    #     exp = models.IntegerField(default=3)
    # else:
    name = models.CharField(max_length=45, default="Goblin")
    max_hp = models.IntegerField(default=20)
    hp = models.IntegerField(default=20)
    damage_min = models.IntegerField(default=2)
    damage_max = models.IntegerField(default=4)
    exp = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Slime(models.Model):
#     name = models.CharField(max_length=45, default="Slime")
#     max_hp = models.IntegerField(default=15)
#     hp = models.IntegerField(default=15)
#     damage_min = models.IntegerField(default=1)
#     damage_max = models.IntegerField(default=2)
#     exp = models.IntegerField(default=3)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Monster(models.Model):
