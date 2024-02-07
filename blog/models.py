from django.db import models


class post (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return "{}_{}".format(self.id, self.title)

    class Meta:
        db_table = 'پست'
# Create your models here.
