from __future__ import unicode_literals

from django.db import models
from travel.models import User
from offer.models import Enlist

class Reservation(models.Model):
    uid = models.ForeignKey(User, on_delete = models.CASCADE)
    eid = models.ForeignKey(Enlist, on_delete = models.CASCADE)
    from_loc = models.CharField(max_length = 250)
    to_loc = models.CharField(max_length = 250)
    start_date = models.DateField()
    status = models.BooleanField(default = False)


    def __str__(self):
        return self.from_loc + '-' + self.to_loc
