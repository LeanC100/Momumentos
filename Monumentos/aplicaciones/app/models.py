from django.db import models

# Create your models here.


class date_monumento (models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    height = models.PositiveIntegerField()
    creation = models.PositiveIntegerField()
