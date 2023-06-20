from uuid import uuid4
from django.db import models



class Location(models.Model):
    id = models.UUIDField(primary_key=True, editable=False),
    fsq_id = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(null=True)
    country = models.CharField(max_length=30,null=True)
    region = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=155,null=True)
