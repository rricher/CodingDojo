from __future__ import unicode_literals
import re
from django.db import models

class LoginManager(models.Manager):
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

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # if Book.objects.filter(title = postData['title']):
        #     title_found = True
        # else:
        #     title_found = False
        if len(postData['title']) < 1:
            errors['title'] = "Title is required and must be unique"
        if len(postData['desc']) < 5:
            errors['desc'] = "Description must be at least 5 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = LoginManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # favorites = books I have favorited
    # created_books = books I have reated

class Book(models.Model):
    creator = models.ForeignKey(User, related_name="created_books", on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name="favorites")
    title = models.CharField(max_length=255)
    desc = models.TextField()
    objects = BookManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)