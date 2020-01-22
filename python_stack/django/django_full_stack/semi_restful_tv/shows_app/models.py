from __future__ import unicode_literals
from django.db import models

class Manager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if not len(postData['description']) == 0 and len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        if len(postData['release_date']) < 1:
            errors["release_date"] = "Realease date needs a date that is not the current date."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    creates_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = Manager()