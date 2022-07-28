from email.quoprimime import body_check
from turtle import update
from venv import create
from django.db import models

class Note(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:30]
    
    class Meta:
        ordering = ['-updated']