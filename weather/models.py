from django.db import models

# Create your models here.
class city(models.Model):
    city = models.CharField(max_length=200)