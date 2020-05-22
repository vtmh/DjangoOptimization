from django.db import models
from django.utils import timezone

# Create your models here.

class LoginEntry(models.Model):
    time = models.DateField(default=timezone.now)
