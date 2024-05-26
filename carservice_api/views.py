# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from carservice_api import models
# from .serializer import CarsSerializer
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi

# # Create your views here.
# cars_response = openapi.Response('Success', CarsSerializer)
# @swagger_auto_schema(
#     method='get',
#     responses={
#         200: cars_response,
#         404: 'Not Found',
#     }
# )
# @api_view(['GET'])
# def getAll(request):
#     data = models.Cars.objects.all()
#     serializer = CarsSerializer(data, many=True)
#     return Response(serializer.data)