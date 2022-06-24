from django.db import models
from django.forms import CharField, DateTimeField

# Create your models here.
class Post(models.Model):
    title = models.CharField(unique=True, null=False,max_length=200)
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title