from django.db import models
class post (models.Model):
    title=models.CharField(max_length=255)
    detail=models.TextField()
# Create your models here.
