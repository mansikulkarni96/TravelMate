from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length = 250)
    lname = models.CharField(max_length = 250)
    phone = models.IntegerField()
    email = models.CharField(max_length = 250)
    password = models.CharField(max_length = 250)
    rating = models.FloatField(default=5.0)


    def __str__(self):
        return self.fname + '-' + self.lname
