from platform import release
from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.IntegerField()
    review = models.TextField()
    
