from gc import is_finalized
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null = True)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_finished = models.BooleanField(default = False, blank = True)
    