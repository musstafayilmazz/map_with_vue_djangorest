from rest_framework import serializers
from location_api.models import Location

class LocationSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only = True)
    fsq_id = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    address = serializers.CharField()
    country = serializers.CharField()
    region = serializers.CharField()
    name = serializers.CharField()
    