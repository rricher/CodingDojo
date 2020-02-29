from django.db import models
from django import forms

class User(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=255)