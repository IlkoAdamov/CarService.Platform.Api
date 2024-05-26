from rest_framework import serializers
from carservice_api import models
from .serviceserializers import ServiceSerializer

class MaintenanceSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = models.Maintenance
        fields = ('id', 'car_id', 'type', 'created_at', 'mileage', 'service')
        extra_kwargs = {'car_id': {'required': True}}
        extra_kwargs = {'service': {'required': False}}

    created_at = serializers.DateField(format='%B %d, %Y')
    
    def create(self, validated_data):
        maintenance = models.Maintenance.objects.create(**validated_data)
        return maintenance