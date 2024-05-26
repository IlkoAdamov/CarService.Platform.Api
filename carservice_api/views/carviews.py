from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from carservice_api import models
from carservice_api import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

cars_get_response = openapi.Response('OK', serializers.CarSerializer(many=True))
@swagger_auto_schema(method='get', responses={200: cars_get_response, 500: 'Internal server error'})
@api_view(['GET'])
def get_list_of_cars(request, *args, **kwargs):
    """List of all cars items"""

    try:
        data = models.Car.objects.all()

        serializer = serializers.CarSerializer(data, many=True)
    except:
        return Response(serializer.error, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.data, status= status.HTTP_200_OK)

@swagger_auto_schema(method='POST',
    request_body= serializers.CarSerializer,
    responses={201: openapi.Response('Created', serializers.CarSerializer), 400: 'Bad Request', 500: 'Internal Server Error'})
@api_view(['POST'])
def create_car_item(request, *args, **kwargs):
    try:
        data = {
            'id': request.data.get('id'),
            'vin': request.data.get('vin'),
            'brand': request.data.get('brand'),
            'model': request.data.get('model'),
            'fuel': request.data.get('fuel'),
            'power': request.data.get('power'),
            'horse_power': request.data.get('horse_power'),
            'plate': request.data.get('plate')
        }
        serializer = serializers.CarSerializer(data= data)
    except:
        return Response(serializer.error, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

request_id = openapi.Parameter('id', openapi.IN_PATH, description="car id", type=openapi.TYPE_INTEGER)
@swagger_auto_schema(method='PUT',
    manual_parameters=[request_id],
    request_body= serializers.CarSerializer,
    responses={200: openapi.Response('OK', serializers.CarSerializer), 400: 'Bad Request', 500: 'Internal Server Error'})
@api_view(['PUT'])
def update_car_item(request, id, *args, **kwargs):
    try:
        data = {
            'id': request.data.get('id'),
            'vin': request.data.get('vin'),
            'brand': request.data.get('brand'),
            'model': request.data.get('model'),
            'fuel': request.data.get('fuel'),
            'power': request.data.get('power'),
            'horse_power': request.data.get('horse_power'),
            'plate': request.data.get('plate')
        }

        car_object = models.Car.objects.get(id = id)

        serializer = serializers.CarSerializer(instance= car_object, data= data, partial= True)

    except models.Car.DoesNotExist:
        return Response({"message": f"Object with id {id} does not exists"}, status= status.HTTP_404_NOT_FOUND) 
    except:
        return Response(serializer.error, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
            
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
# vin_param = openapi.Parameter('vin', openapi.IN_BODY, description="VIN number", type=openapi.TYPE_STRING)
# brand_param = openapi.Parameter('brand', openapi.IN_BODY, description="Car brand", type=openapi.TYPE_STRING)
# model_param = openapi.Parameter('model', openapi.IN_BODY, description="Car model", type=openapi.TYPE_STRING)
# fuel_param = openapi.Parameter('fuel', openapi.IN_BODY, description="Type of fuel", type=openapi.TYPE_STRING)
# power_param = openapi.Parameter('power', openapi.IN_BODY, description="Power in kW", type=openapi.TYPE_INTEGER)
# horse_power_param = openapi.Parameter('horse power', openapi.IN_BODY, description="Horse power", type=openapi.TYPE_INTEGER)
# plate_param = openapi.Parameter('plate', openapi.IN_BODY, description="Plate number", type=openapi.TYPE_STRING)
# cars_post_response = openapi.Response('Created', serializers.CarsSerializer(many=True))
# @swagger_auto_schema(method='post', manual_parameters=[vin_param, brand_param, model_param, fuel_param, power_param, horse_power_param, plate_param], responses={201: cars_post_response, 400: 'Bad Request'})

# cars_post_response = openapi.Response('Created', django.core.serializers.serialize('json', models.Car.objects.all()))
# @swagger_auto_schema(method='POST', request_body=openapi.Schema(
#     type=openapi.TYPE_OBJECT, 
#     properties={
#         'vin_param': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         'brand_param': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         'model_param': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         'fuel_param': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         'power_param': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
#         'horse_power_param': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
#         'plate_param': openapi.Schema(type=openapi.TYPE_STRING, description='string')
#     },
#     responses={201: cars_post_response, 400: 'Bad Request'}
# ))
# @api_view(['POST'])
# def create_car_item(request, *args, **kwargs):
#     """create a new car item"""
#     data = {
#         'vin': request.data.get('vin_param'),
#         'brand': request.data.get('brand_param'),
#         'model': request.data.get('model_param'),
#         'fuel': request.data.get('fuel_param'),
#         'power': request.data.get('power_param'),
#         'horse_power': request.data.get('horse_power_param'),
#         'plate': request.data.get('plate_param')
#     }

#     serializer = serializers.CarSerializer(data= data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status= status.HTTP_201_CREATED)
        
#     return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)