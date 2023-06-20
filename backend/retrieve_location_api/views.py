from rest_framework.decorators import api_view
from rest_framework.response import Response
from retrieve_location_api.models import LatLong
from retrieve_location_api.serializer import LatLongSerializer
from rest_framework import status


@api_view(['GET'])
def location_list(request):
    """This method created for listing posted and stored latitude&longitude data

    Args:
        request (request): _

    Returns:
        _type_: serialized data
    """
    location = LatLong.objects.all()
    serializer = LatLongSerializer(location, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def location_create(request):
    """This Method crated for retrieving data to foursquare search api

    Args:
        request (request): 

    Returns:
        _type_: serailez data
    """
    serializer = LatLongSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    #{
#"latitude" : 23.5,
#"longitude" : 16.7
#}
