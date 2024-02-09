from django.db import models
from django_jalali.db import models as jmodels


class contacts (models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    created_time = jmodels.jDateTimeField(auto_now_add=True)
    update_time= jmodels.jDateTimeField(auto_now=True)
# Create your models here.
