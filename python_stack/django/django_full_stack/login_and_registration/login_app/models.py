from __future__ import unicode_literals
import re
from django.db import models

class loginManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if User.objects.filter(email = postData['email']):
            email_found = True
        else:
            email_found = False

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name should be longer than two characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name should be longer than two characters"
        if not EMAIL_REGEX.match(postData['email']) or email_found == True:
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password_length'] = "Password should be at least 8 characters"
        if not postData['password'] == postData['confirm_password']:
            errors['password_confirm'] = "Passwords should match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = loginManager()