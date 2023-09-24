from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    content = models.CharField(max_length=300)