from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from carservice_api import models
from carservice_api import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

service_get_response = openapi.Response('OK', serializers.ServiceSerializer(many=True))
maintenance_id_param = openapi.Parameter('maintenance_id', openapi.IN_PATH, description="maintenance id", type=openapi.TYPE_INTEGER)
@swagger_auto_schema(method='get', manual_parameters=[maintenance_id_param], responses={200: service_get_response, 404: 'Not Found', 500: 'Internal server error'})
@api_view(['GET'])
def get_list_of_service_byMaintenanceId(request, maintenance_id, *args, **kwargs):
    """List of service items getting by maintenance Id"""
    try:
        data = models.Service.objects.filter(maintenance_id = maintenance_id)

        serializer = serializers.ServiceSerializer(data, many=True)

        if len(serializer.data) == 0:
            raise(models.Service.DoesNotExist)
    except models.Service.DoesNotExist:
        return Response({"message": f"Objects with maintenance id = {maintenance_id} does not exists"}, status= status.HTTP_404_NOT_FOUND)
    except:
        return Response(serializer.error, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.data, status= status.HTTP_200_OK)

@swagger_auto_schema(method='POST',
    request_body= serializers.ServiceSerializer,
    responses={201: openapi.Response('Created', serializers.CarSerializer), 400: 'Bad Request', 500: 'Internal Server Error'})
@api_view(['POST'])
def create_service_item(request, *args, **kwargs):
    try:
        data = {
            'maintenance_id': request.data.get('maintenance_id'),
            'service_type': request.data.get('service_type'),
            'title': request.data.get('title'),
            'description': request.data.get('description')
        }
        serializer = serializers.ServiceSerializer(data= data)
    except:
        return Response(serializer.error, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)