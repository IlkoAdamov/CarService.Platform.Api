from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from carservice_api import models
from carservice_api import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

maintenance_get_response = openapi.Response('OK', serializers.MaintenanceSerializer(many=True))
@swagger_auto_schema(method='get', responses={200: maintenance_get_response, 500: 'Internal server error'})
@api_view(['GET'])
def get_list_of_maintenances(request, *args, **kwargs):
    """List all the maintenance items"""

    try:
        data = models.Maintenance.objects.all()

        serializer = serializers.MaintenanceSerializer(data, many=True)
    except:
        return Response(serializer.error, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.data, status= status.HTTP_200_OK)


car_id_param = openapi.Parameter('car_id', openapi.IN_PATH, description="car id", type=openapi.TYPE_INTEGER)
@swagger_auto_schema(method='get', manual_parameters=[car_id_param], responses={200: maintenance_get_response, 404: 'Not Found', 500: 'Internal server error'})
@api_view(['GET'])
def get_list_of_maintenances_byCarId(request, car_id, *args, **kwargs):
    """List of maintenance items extracted by car id"""
    try:
        data = models.Maintenance.objects.filter(car_id = car_id)

        serializer = serializers.MaintenanceSerializer(data, many=True)

        if len(serializer.data) == 0:
            raise(models.Maintenance.DoesNotExist)
    except models.Maintenance.DoesNotExist:
        return Response({"message": f"Objects with car id = {car_id} does not exists"}, status= status.HTTP_404_NOT_FOUND) 
    except:
        return Response(serializer.error, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.data, status= status.HTTP_200_OK)

@swagger_auto_schema(method='POST',
    request_body= serializers.MaintenanceSerializer,
    responses={201: openapi.Response('Created', serializers.MaintenanceSerializer), 400: 'Bad Request', 500: 'Internal Server Error'})
@api_view(['POST'])
def create_maintenance_item(request, *args, **kwargs):
    """create a new maintenance item"""
    try:
        data = {
            'type': request.data.get('type'),
            'car_id': request.data.get('car_id'),
            'created_at': request.data.get('created_at'),
            'mileage': request.data.get('mileage'),
        }
        serializer = serializers.MaintenanceSerializer(data= data)
    except:
        return Response(serializer.error, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
# @swagger_auto_schema(method='POST', request_body=openapi.Schema(
#     type=openapi.TYPE_OBJECT, 
#     properties={
#         'type_param': openapi.Schema(type=openapi.TYPE_INTEGER, description='[service: 1, repairs: 2]'),
#         'car_id_param': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
#     },
#     responses={201: 'Created', 400: 'Bad Request'}
# ))
# @api_view(['POST'])
# def create_maintenance_item(request, *args, **kwargs):
#     """create a new maintenance item"""
#     data = {
#         'type': request.data.get('type_param'),
#         'car_id': request.data.get('car_id_param'),
#     }

#     serializer = serializers.MaintenanceSerializer(data= data)
    
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status= status.HTTP_201_CREATED)
        
#     return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)