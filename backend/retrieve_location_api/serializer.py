from rest_framework import serializers
from retrieve_location_api.models import LatLong

class LatLongSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    
    
    def create(self,validated_data):
        return LatLong.objects.create(**validated_data)