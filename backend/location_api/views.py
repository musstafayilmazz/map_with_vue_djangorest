from django.http import JsonResponse
from django.shortcuts import render
from location_api.serializer import LocationSerializer
from location_api import serializer
from retrieve_location_api.models import LatLong
from rest_framework.decorators import api_view 
from rest_framework.response import Response
import requests
from location_api.models import Location
import rest_framework.status

@api_view(['GET'])
def location_record(request):
    """This Method calls foursquare search API. After finish,record values to database.

    Args:
        request (request): -

    Returns:
        Serialized Json File
    """
    last_latlong = LatLong.objects.last()
    
    latitude = last_latlong.latitude
    longitude = last_latlong.longitude
    
    url = f"https://api.foursquare.com/v3/places/search?ll={latitude}%2C{longitude}"
    headers = {
    "accept": "application/json",
    "Authorization": "fsq38jf5s6BtxsM5GasJ/3pdhr7HlOSL2O6cjpiwegCvd90="
    }
    
    response = requests.get(url, headers=headers)
    api_data = response.json()
    
    results = api_data.get('results',[])
    formatted_results = []
    for result in results:
        fsq_id = result.get('fsq_id')
        latitude = result.get('geocodes', {}).get('main', {}).get('latitude')
        longitude = result.get('geocodes', {}).get('main', {}).get('longitude')
        address = result.get('location', {}).get('formatted_address')
        country = result.get('location', {}).get('country')
        region = result.get('location', {}).get('region')
        name = result.get('name')
        id = result.get('id')

        location = Location(
        id = id,
        fsq_id=fsq_id,
        latitude=latitude,
        longitude=longitude,
        address=address,
        country=country,
        region=region,
        name=name
    )
        formatted_result = {
            'id': id,
            'fsq_id': fsq_id,
            'latitude': latitude,
            'longitude': longitude,
            'address': address,
            'country': country,
            'region': region,
            'name': name
        }
        formatted_results.append(formatted_result)
        
        location.save()
        
        related_places = result.get('related_places', {}).get('children',[])
        for related_place in related_places:
            fsq_id = related_place.get('fsq_id')
            latitude = result.get('geocodes', {}).get('main', {}).get('latitude')
            longitude = result.get('geocodes', {}).get('main', {}).get('longitude')
            address = result.get('location', {}).get('formatted_address')
            country = result.get('location', {}).get('country')
            region = result.get('location', {}).get('region')
            name = related_place.get('name')
            
            location = Location(
            id = id,
            fsq_id=fsq_id,
            latitude=latitude,
            longitude=longitude,
            address=address,
            country=country,
            region=region,
            name=name
            )
            location.save()
            formatted_result = {
            'id': id,
            'fsq_id': fsq_id,
            'latitude': latitude,
            'longitude': longitude,
            'address': address,
            'country': country,
            'region': region,
            'name': name
        }
            formatted_results.append(formatted_result)
            
    
            
            
        
    
    return JsonResponse(formatted_results,safe=False)
    
@api_view(['GET'])
def location_list(request):
    """This method calls all recorded data with all keys.

    Args:
        request (request): -

    Returns:
        _type_: serialized data
    """
    location = Location.objects.all()
    serializer = LocationSerializer(location,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def coordinates(request):
    """This method call all data with in a format 

    Args:
        request (request): 

    Returns:
        _type_: seralized data in format {"name" : name , "latitude" : latitude, "longitude" : longitude }
    """
    locations = Location.objects.all()
    data = []

    for location in locations:
        data.append({
            'name' : location.name,
            'latitude': location.latitude,
            'longitude': location.longitude
        })

    return Response(data)