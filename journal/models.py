from django.db import models
from django.utils import timezone

# Create your models here.

class Journal(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=300)
    favourite = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    photo = models.FileField(upload_to='')

    def __str__(self):
        return self.title 


    
