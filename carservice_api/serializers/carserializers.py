from rest_framework import serializers
from carservice_api import models
from .maintenanceserializers import MaintenanceSerializer

class CarSerializer(serializers.ModelSerializer):
    maintenance = MaintenanceSerializer(many=True, read_only=True)

    class Meta:
        model = models.Car
        fields = ('id', 'vin', 'brand', 'model', 'fuel', 'power', 'horse_power', 'plate', 'maintenance')
        extra_kwargs = {'maintenance': {'required': False}}
    
    def create(self, validated_data):
        car = models.Car.objects.create(**validated_data)
        return car