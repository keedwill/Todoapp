from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
