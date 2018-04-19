from django.db import models

# Create your models here.
class Comment(models.Model):
     food = models.CharField(max_length=180, null=True, blank=True)
     address = models.CharField(max_length=180, null=True, blank=True)