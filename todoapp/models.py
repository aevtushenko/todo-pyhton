from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    hashed_password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.email


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    isComplete = models.BooleanField(default=False)
    collaborators = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title

    
