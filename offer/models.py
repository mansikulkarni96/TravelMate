from __future__ import unicode_literals

from django.db import models
from travel.models import User

class Enlist(models.Model):
    uid = models.ForeignKey(User, on_delete = models.CASCADE)
    car_model = models.CharField(max_length = 250)
    car_no = models.IntegerField()
    seat = models.IntegerField()
    from_loc = models.CharField(max_length = 250)
    to_loc = models.CharField(max_length = 250)
    fare = models.FloatField(default=5.0)
    start_time = models.TimeField()
    return_time = models.TimeField()
    start_date = models.DateField()
