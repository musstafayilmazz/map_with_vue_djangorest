from django.db import models


# I created A model here, Id is auto created pk field.

class LatLong(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
