from django.db import models

class contacts (models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    update_time= models.TimeField(auto_now=True)
# Create your models here.
